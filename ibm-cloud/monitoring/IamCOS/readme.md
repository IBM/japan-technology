# IBM Cloud Simple IAM/COS health checker

As of 6 June 2025: Created by Akira Onishi

Updated on 7 June 2025: Co-worked with Jason McGee, implemented 2 key items.
* Added custom User-Agent name "IamCOS/1.0 (Bee)".
* Added caching for API result for safeguarding to invoke IAM/COS services.
Updated on 8 June 2025:
* Modified some topics in this document.

This Node.js application provides a simple web dashboard and API endpoints to check the status of IBM Cloud IAM and Cloud Object Storage (COS).  
It is designed to be easy to deploy on Azure App Service or any Node.js environment.

(Note) Do not change the cache duration less than 10 seconds.

## Features

- **Web Dashboard**: View IAM and COS status in your browser.
- **REST API**: `/status/iam` and `/status/cos` endpoints return JSON status.
- **10-second cache**: Reduces load on IBM Cloud APIs.
- **Custom User-Agent**: All API calls use `IamCOS/1.0 (Bee)`.

## Prerequisites

- Node.js **18.x** or later (LTS recommended)
- IBM Cloud API Key and COS HMAC credentials
- (Recommended) Azure App Service or any Node.js hosting

## How to run this
### local machine
* Install [Node.js](https://nodejs.org/en/download) 
* Open your Terminal (macOS), PowerShell (Windows) , Linux on Windows, or other shell on Linux

  create a new folder like "cloudtool" or go to your work folder.

Example:

```
cd ~
mkdir cloudtool
cd cloudtool
```

* Download [this file](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/IamCOS20250607.zip).  And, Unzip the zip file.

macOS/Linux

```
wget https://github.com/IBM/japan-technology/raw/refs/heads/main/ibm-cloud/monitoring/IamCOS/IamCOS20250607.zip
unzip IamCOS20250607.zip
```
    
if you work with Windows (PowerShell)

```
wget https://github.com/IBM/japan-technology/raw/refs/heads/main/ibm-cloud/monitoring/IamCOS/IamCOS20250607.zip -outfile t.zip
Expand-Archive t.zip .
```


* Install required Node.js packages.  Type the following command in the extracted folder.
```
npm install
```

　　(Windows only) If you have an execution policy error to run "npm install", run
  ```
  Set-ExecutionPolicy RemoteSigned
  ```

(Required open PowerShell as Administrator).  Then,

```
npm install
``` 
again.

* Set required environment variables [below](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/readme.md#required-environment-variables).  An easy way to do this, create .env file in your extracted folder by Visual Studio Code or other text editor.
* Type ```node --env-file=.env server.js```
* Open http://localhost:3001 in your browser to run the app
* You will see the status of IAM and COS.

### [Microsoft Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/)
* Create a new Web App with Linux OS
* Set required environment variables as "Application Settings" in the portal instead of using a `.env` file.
(Deployment option 1)
* Deploy [this file](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/IamCOS20250607.zip)
   
or
(Deploymenet option 2)
* Unzip [this file](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/IamCOS20250607.zip)
* Open the extracted folder with Visual Studio Code
* Install "Azure App Service" VS Code extension
* Deploy the folder with the extension

## Files

* [server.js](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/server.js): API server to check the IAM/COS health.
* [public/default.html](https://github.com/IBM/japan-technology/blob/main/ibm-cloud/monitoring/IamCOS/public/default.html): Web page to invoke 2 APIs throught status.js
* [public/status.js](https://github.com/IBM/japan-technology/tree/main/ibm-cloud/monitoring/IamCOS/public/js): JavaScript to connect/invoke API on server.js
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

Please use the .env template if you would like.
```
#.env
PORT=3001
IBM_API_KEY=<your_ibm_api_key>
COS_BUCKET=<your_cos_bucket_name>
COS_REGION=<your_cos_region like "jp-tok">
FILE_KEY=<your_filename in the cos_bucket>
COS_HMAC_ACCESS_KEY_ID=<your_cos_hmac_access_key_id>
COS_HMAC_SECRET_ACCESS_KEY=<your_cos_hmac_secret_access_key>
```

## API spec (server.js)

- GET /
    - Return public/default.html to host the Web UI

- GET /status/iam
    - Return the result after invoking IAM API to create new access token by API key
    - Return value: JSON {status, message}
        - status: OK, Error, Down
        - Example: 
```json
{
  "status": "ok",
  "message": "IAM is working"
}
```

- GET /status/cos
    - Return the result after reading a file in Cloud Object Storage by S3 API.
    - Return value: JSON {status, message}
        - status: ok, error
        - Example:
```json
{
  "status": "ok",
  "message": "COS is working"
}
```

