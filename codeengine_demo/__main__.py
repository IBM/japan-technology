# -*- coding: utf-8 -*-

import sys
import traceback
import ibm_boto3
import ibm_db
from ibm_botocore.client import Config, ClientError
from datetime import datetime, timedelta, timezone
import re

"""
This exception is made for separating error occuring in copy process from fatal error.
Even if this exception is raised, this program does nothing for this exception and goes next process.
"""
class Copy_fail_exception(Exception):
    pass


class Readxlsx:
    # The constructer checks number of parameter, declares variables and creates resource of ICOS.
    def __init__(self, dict_param):
        print("INFO : IPY2100 parameter check started.")
        if len(dict_param) != 11:
            print("ERROR : EPY2100 parameter check failed. Please check parameters.")
            sys.exit()
        print("INFO : IPY2101 parameter check completed.")
        self.pvvp_cos_auth_endpoint = dict_param["Arg_cos_auth_endpoint"]
        self.pvvp_cos_api_key_id = dict_param["Arg_cos_api_key_id"]
        self.pvvp_cos_resource_crn = dict_param["Arg_cos_resource_crn"]
        self.pvvp_cos_endpoint = dict_param["Arg_cos_endpoint"]
        self.pvvp_trigger_bucket = dict_param["Arg_trigger_bucket"]
        self.pvvp_proc_queued_bucket = dict_param["Arg_process_queued_loc"].split("/")[0]
        self.pvvp_proc_queued_loc = dict_param["Arg_process_queued_loc"].split("/")[1]
        self.cos, self.client = self.create_icos_resource()
        
    def create_icos_resource(self):
        print("INFO : IPY2102 Creating ICOS resource")
        try:
            cos = ibm_boto3.resource("s3",
                         ibm_api_key_id=self.pvvp_cos_api_key_id,
                         ibm_service_instance_id=self.pvvp_cos_resource_crn,
                         ibm_auth_endpoint=self.pvvp_cos_auth_endpoint,
                         config=Config(signature_version="oauth"),
                         endpoint_url=self.pvvp_cos_endpoint
                         )

            client = ibm_boto3.client("s3",
                         ibm_api_key_id=self.pvvp_cos_api_key_id,
                         ibm_service_instance_id=self.pvvp_cos_resource_crn,
                         ibm_auth_endpoint=self.pvvp_cos_auth_endpoint,
                         config=Config(signature_version="oauth"),
                         endpoint_url=self.pvvp_cos_endpoint
                         )
            print("INFO : IPY2103 Finished Creating ICOS resource")
        except Exception as e:
            e_msg = f"""ERROR : EPY2101 ICOS connection failed.
            {traceback.format_exc()}"""
            print(e_msg)
            sys.exit()

        return cos, client

   
    def get_file_list(self):
        print("INFO : IPY2104 File list aquisition process started")
        try:
            files = self.cos.Bucket(self.pvvp_trigger_bucket).objects.filter()
            conf = ".+\.xlsx"
            file_list = [k.key for k in files if re.fullmatch(conf, k.key)]
        except Exception as e:
            e_msg = f"""ERROR : EPY2102 File list to df process failed.trigger_bucket={self.pvvp_trigger_bucket}
            {traceback.format_exc()}"""
            print(e_msg)
            sys.exit()
        print("INFO : IPY2106 File list to df process finished")

        if len(file_list) == 0:
            print("WARNING : WPY2100 No .xlsx file is found in trigger bucket.")
        print("INFO : IPY2107 File list aquisition process finished.")
        return file_list

    
    def timestamp_filename(self, filename):
        print("INFO : IPY2108 File ({}) timestamp add process started.".format(filename))
        try:
            JST = timezone(timedelta(hours=+9), 'JST')
            timestamp = datetime.now(JST).strftime("%Y%m%d%H%M%S%f")[0:17]
            timestamped_xlsx_name = timestamp + "_" + filename
            print("INFO : IPY2109 timestamp add process finished. Timestamped file name: {} ".format(timestamped_xlsx_name))
        except Exception as e:
            e_msg = f"""INFO : EPY2103 File ({filename}) timestamp add process failed.
            {traceback.format_exc()}"""
            print(e_msg)
            sys.exit()
        return timestamped_xlsx_name, int(timestamp)

    def copy_file(self, cp_file_from, cp_file_to, bucket_from, bucket_to):
        print("INFO : IPY2110 Object copy from {}/{} to {}/{} process started".format(bucket_from, cp_file_from, bucket_to, cp_file_to))
        try:
            copy_source = {
                'Bucket':bucket_from,
                'Key':cp_file_from
                }
            cos_copy_to = self.cos.Bucket(bucket_to)
            obj = cos_copy_to.Object(cp_file_to)
            obj.copy(copy_source)
            print("INFO : IPY2111 Object copy process finished")
        except Exception as e:
            """
            There would be a problem where the connection to the cloud is broken, but it will be momentary.
            Therefore, this program does nothing for this exception and goes next process.Next time, this file will be processed.
            """
            e_msg = f"""ERROR : EPY2104 Object copy from {bucket_from}/{cp_file_from} to {bucket_to}/{cp_file_to} process failed.
            {traceback.format_exc()}"""
            print(e_msg)
            raise Copy_fail_exception

    def delete_file(self, delete_file, delete_bucket):
        print("INFO : IPY2112 Object ({}) delete process started".format(delete_file))
        try:
            response = self.client.delete_object(Bucket=delete_bucket, Key=delete_file)
            print("INFO : IPY2113 Object ({}) delete process finished".format(delete_file))
        except Exception as e:
            """
            The program do nothing for this exception, but manual recovery process is needed.
            """
            e_msg = f"""ERROR : EPY2105 Object ({delete_file}) delete from ({delete_bucket}) bucket process failed. Proceed.
            {traceback.format_exc()}"""
            print(e_msg)

         
    def exec_file_list(self, file_list):
        for index, xlsx_name in enumerate(file_list):
            print("INFO : IPY2116 File ({}) execution process started.".format(xlsx_name))
            try:
                timestamped_xlsx_name, timestamp = self.timestamp_filename(xlsx_name)
                file_in_que = self.pvvp_proc_queued_loc + "/" + timestamped_xlsx_name
                self.copy_file(xlsx_name, file_in_que, self.pvvp_trigger_bucket, self.pvvp_proc_queued_bucket)
                self.delete_file(xlsx_name, self.pvvp_trigger_bucket)
            except Copy_fail_exception:
                """
                There would be a problem where the connection to the cloud is broken, but it will be momentary.
                Therefore, this program does nothing for that error and goes next process.
                """
                pass


def main(dict):
    try:
        read_xlsx_inst = Readxlsx(dict)
        file_list = read_xlsx_inst.get_file_list()
        read_xlsx_inst.exec_file_list(file_list)
        print("INFO : IPY2199 Finished the program.")
    except SystemExit as e:
        print("ERROR : EPY2199 Exit the program.")
    return { 'message' : 'python implementation finished'}
