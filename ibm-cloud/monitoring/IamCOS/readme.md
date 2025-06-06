# Simple IAM/COS health checker

As of 6 June 2025: Created by Akira Onishi

This is a simpler Node.js web application to check the IAM/COS health.

* IAM: Try to create new access token via IAM with API key. You see "IAM is working" or an error message.
* COS: Try to read exising file via S3 API.  You get "COS is working" or an error message.

Here is a [zip file](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/iamcos20250606.zip).
Please deploy the following files into Node.js enabled environement with required environment variables [below](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/readme.md#required-environment-variables).

I confirm it works with Microsoft Azure App Service with Node.js.  
And you can run it on your local machine and/or other server/cloud platform by installing [Node.js](https://nodejs.org/en/download) and related packages with:
"npm install" command.


* [server.js](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/server.js): API server to check the IAM/COS health.
* [public/default.html](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/public/default.html): Web page to invoke 2 APIs throught status.js
* [public/status.js](https://github.com/IBM/japan-technology/tree/main/ibm-cloud/monitoring/IamCOS/public/js): JavaScript to connect/invoke API
* [package.json](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/package.json): Node.js project settings. You can run "npm install" to required package into your environment.
* [package-lock.json](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/package-lock.json): packages list for npm (Node Package Manager)

## Required Environment variables
This repository has no value samples for security reason.

* IBM_API_KEY: IBM Cloud API Key.  You can create it at [API Keys](https://cloud.ibm.com/iam/apikeys) on IBM Cloud Console.
* COS_BUCKET: Cloud Object Storage Bucket name
* COS_REGION: Cloud Object Storage region name (Find the region name from [here](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints)
* FILE_KEY: File name in the COS_BUCKET
* COS_HMAC_ACCESS_KEY_ID: [HMAC](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-uhc-hmac-credentials-main) access_key_id
* COS_HMAC_SECRET_ACCESS_KEY: HMAC secret_access_key

## API spec (server.js)

- /
    - Send public/default.html to requester

- /status/iam
    - Return the result after invoking IAM API to create new access token by API key
    - Return value: JSON {status, message}
        - status: OK, Error, Down

- /status/cos
    - Return the result after reading a file in Cloud Object Storage by S3 API.
    - Return value: JSON {status, message, content}
        - status: OK, Error, Down

