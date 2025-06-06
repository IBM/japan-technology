// Special Thanks Jason McGee 
console.log(process.version)
const express = require('express');
const AWS = require('aws-sdk');
const cors = require('cors');
const path = require('path');
const app = express();

// fetch to use in Node.js
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

// Use .env or environment variable
const PORT = process.env.PORT || 3001;
const IBM_API_KEY = process.env.IBM_API_KEY;
const COS_BUCKET = process.env.COS_BUCKET;
const COS_REGION = process.env.COS_REGION;
const FILE_KEY = process.env.FILE_KEY;
const COS_HMAC_ACCESS_KEY_ID = process.env.COS_HMAC_ACCESS_KEY_ID;
const COS_HMAC_SECRET_ACCESS_KEY = process.env.COS_HMAC_SECRET_ACCESS_KEY;

const USER_AGENT = 'IamCOS/1.0 (Bee)';

console.log('USER_AGENT:', USER_AGENT);
//console.log('COS_HMAC_ACCESS_KEY_ID:', COS_HMAC_ACCESS_KEY_ID);
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

// Cache variables
let iamCache = null;
let iamCacheTime = 0;
let cosCache = null;
let cosCacheTime = 0;
const CACHE_DURATION = 10 * 1000; // 10 seconds

app.use(cors());

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'default.html'));
});

app.use(express.static(path.join(__dirname, 'public')));

app.get('/status/iam', async (req, res) => {
  const now = Date.now();
  if (iamCache && (now - iamCacheTime < CACHE_DURATION)) {
    console.log('IAM: cache hit');
    return res.json(iamCache);
  }
  try {
    console.log('IAM: cache miss');
    const params = new URLSearchParams();
    params.append('grant_type', 'urn:ibm:params:oauth:grant-type:apikey');
    params.append('apikey', IBM_API_KEY);
    const response = await fetch('https://iam.cloud.ibm.com/identity/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'User-Agent': USER_AGENT
      },
      body: params
    });
    let result;
    if (response.status === 500) {
      result = { status: 'down', message: 'IAM is not working' };
    } else if (!response.ok) {
      result = { status: 'error', message: `IAM error: HTTP ${response.status}` };
    } else {
      result = { status: 'ok', message: 'IAM is working' };
    }
    iamCache = result;
    iamCacheTime = now;
    return res.json(result);
  } catch (err) {
    const errorResult = { status: 'error', message: 'IAM check failed: ' + err };
    iamCache = errorResult;
    iamCacheTime = now;
    return res.json(errorResult);
  }
});

app.get('/status/cos', async (req, res) => {
  const now = Date.now();
  if (cosCache && (now - cosCacheTime < CACHE_DURATION)) {
    console.log('COS: cache hit');
    return res.json(cosCache);
  }
  try {
    console.log('COS: cache miss');
    const params = {
      Bucket: COS_BUCKET,
      Key: FILE_KEY,
    };
    cos.getObject(params, (err, data) => {
      let result;
      if (err) {
        result = { status: 'error', message: `Object Storage error: ${err.message}` };
      } else {
        // result = { status: 'ok', message: 'Object Storage is working', fileContent: data.Body.toString() };
        result = { status: 'ok', message: 'Object Storage is working' };
      }
      cosCache = result;
      cosCacheTime = Date.now();
      return res.json(result);
    });
  } catch (err) {
    const errorResult = { status: 'error', message: 'Object Storage check failed: ' + err };
    cosCache = errorResult;
    cosCacheTime = Date.now();
    return res.json(errorResult);
  }
});

if (require.main === module) {
  // Start the server
  app.listen(PORT, () => console.log(`Status proxy running on http://localhost:${PORT}`));
}

module.exports = app;
