console.log(process.version)
const express = require('express');
const AWS = require('aws-sdk');
const cors = require('cors');
const path = require('path');
const app = express();

// fetchをNode.jsでも使えるように
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

// Use .env or environment variable
const PORT = process.env.PORT || 3001;
const IBM_API_KEY = process.env.IBM_API_KEY;
const COS_BUCKET = process.env.COS_BUCKET;
const COS_REGION = process.env.COS_REGION;
const FILE_KEY = process.env.FILE_KEY;
const COS_HMAC_ACCESS_KEY_ID = process.env.COS_HMAC_ACCESS_KEY_ID;
const COS_HMAC_SECRET_ACCESS_KEY = process.env.COS_HMAC_SECRET_ACCESS_KEY;

const USER_AGENT = 'IamCOS/1.0 (Bee)';  // Add this request from IBM Cloud team

console.log('USER_AGENT:', USER_AGENT);
console.log('COS_HMAC_ACCESS_KEY_ID:', COS_HMAC_ACCESS_KEY_ID);
console.log('COS_HMAC_SECRET_ACCESS_KEY:', COS_HMAC_SECRET_ACCESS_KEY);

// Configure AWS SDK for IBM COS
const cos = new AWS.S3({
  endpoint: `https://s3.${COS_REGION}.cloud-object-storage.appdomain.cloud`,
  accessKeyId: COS_HMAC_ACCESS_KEY_ID,
  secretAccessKey: COS_HMAC_SECRET_ACCESS_KEY,
  region: COS_REGION,
  signatureVersion: 'v4',
  customUserAgent: USER_AGENT
});

app.use(cors());

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'default.html'));
});

app.use(express.static(path.join(__dirname, 'public')));

app.get('/status/iam', async (req, res) => {
  try {
    const params = new URLSearchParams();
    params.append('grant_type', 'urn:ibm:params:oauth:grant-type:apikey');
    params.append('apikey', IBM_API_KEY);
    // get token from iam using the key
    const response = await fetch('https://iam.cloud.ibm.com/identity/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'User-Agent': USER_AGENT
      },
      body: params
    });

    if (response.status === 500) {
      return res.json({ status: 'down', message: 'IAM is not working' });
    }
    if (!response.ok) {
      return res.json({ status: 'error', message: `IAM error: HTTP ${response.status}` });
    }
    return res.json({ status: 'ok', message: 'IAM is working' });
  } catch (err) {
    return res.json({ status: 'error', message: 'IAM check failed: ' + err });
  }
});

app.get('/status/cos', async (req, res) => {
  try {
    // Try to get the specified file from the bucket
    const params = {
      Bucket: COS_BUCKET,
      Key: FILE_KEY,
    };
    cos.getObject(params, (err, data) => {
      if (err) {
        return res.json({ status: 'error', message: `Object Storage error: ${err.message}` });
      }
      return res.json({ status: 'ok', message: 'Object Storage is working', fileContent: data.Body.toString() });
    });
  } catch (err) {
    return res.json({ status: 'error', message: 'Object Storage check failed: ' + err });
  }
});

if (require.main === module) {
  // Start the server
  app.listen(PORT, () => console.log(`Status proxy running on http://localhost:${PORT}`));
}

module.exports = app;
