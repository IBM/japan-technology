# Simple IAM/COS health checker

As of 6 June 2025: Created by Akira Onishi

This is a simpler web application to check the IAM/COS health.
* IAM: Try to create new access token via IAM with API key
* COS: Try to read exising file via S3 API

Please deploy the following files into Node.js enabled environement.  It works with Microsoft Azure App Service with Node.js.  
And you can run it on your local machine and/or other server/cloud platform by setting Node.js andrelated packages.

* server.js: API server to check the IAM/COS health.
* public/default.html: Web page to invoke 2 APIs throught status.js
* public/status.js: JavaScript to connect/invoke API
* package.json: Node.js project settings. 
* package-lock.json: packages list for npm (Node Package Manager)

## Required Environment variables
This repository has no value samples for security reason.

* IBM_API_KEY: IBM Cloud API Key.  You can create it at [API Keys](https://cloud.ibm.com/iam/apikeys) on IBM Cloud Console.
* COS_BUCKET: Cloud Object Storage Bucket name
* COS_REGION: Cloud Object Storage region name (Find the region name from [here](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints)
* FILE_KEY: File name in the COS_BUCKET
* COS_HMAC_ACCESS_KEY_ID: [HMAC](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-uhc-hmac-credentials-main) access_key_id
* COS_HMAC_SECRET_ACCESS_KEY: HMAC secret_access_key

