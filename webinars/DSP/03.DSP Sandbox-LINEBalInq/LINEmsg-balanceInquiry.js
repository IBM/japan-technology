const LINE_ChannelAccessToken = "Sqk62q98jeMuW5f6WKA8EfHn72aggi7HGigLQxSVjQqBb08RbuzujWjOJ9pqgdfbiFFm5Qx0GtLffOgN1AViqvgSgj4ZcIpAX6HaJ0UkW/AiYftLw1utrUm/EQ4lKQvBESALjS5Z02kRWlG7JbDNxgdB04t89/1O/w1cDnyilFU=";
const DSP_APIKey_ClientID     = "6125b5bb-98c5-43a1-9bf7-6a6bd036b302";
const DSP_APIKey_ClientSecret = "dB2wM8tX1rT1pF1cY4jV4aF2kA8kJ0nQ8vV7mV2pC5mR5yJ5yG";

async function main(params) {
  if(params.events && params.events[0].type === "message" ){
    const message = params.events[0].message.text;
    const replyToken = params.events[0].replyToken;
    const userId = params.events[0].source.userId;
    
    let reply = "";
    if(message.includes("残高")){
      /* 本来はLINEユーザIDを元に支店番号、口座種別、口座番号を抽出 */
      const balance = await callSandboxAPI("001", "001", "1234567");
      if(balance){
        reply = "残高は" + balance + "です。";
      } else {
        reply = "残高を取得できませんでした。";
      }
    } else {
      reply = "今日はいい天気ですね。";
    }
    const sent = await callLineReplyAPI(reply, replyToken);
    return { sent: sent, message: reply };
  } else {
    return { message: "Not a LINE Message." };
  }
}

async function callLineReplyAPI(replytext, token){
  const axios = require('axios');
  const lineReplyOption = {
    method : "post",
    url : 'https://api.line.me/v2/bot/message/reply',
    headers : {
      "Authorization" : "Bearer " + LINE_ChannelAccessToken,
      "Content-Type"  : "application/json",
    },
    data : {
      messages :[ {
        "type" : "text",
        "text" : `${replytext}`,
      }],
      replyToken : token,
    }
  }
  try {
    await axios.request(lineReplyOption);
    return true;
  } catch (error) {
    return false;
  }
}

async function callSandboxAPI(branchNumber, accountType, accountNumber) {
  const axios = require('axios');
  const dspOption = {
    method : 'post',
    url : 'https://api.devcom.dsp4f.net/ebb1179jpibmcom-dev/dsp-openapi/ordinarydeposit/v1.2.0/ordinaryDeposit/accounts/balance/inquiry',
    headers: {
      "X-IBM-Client-Id" : DSP_APIKey_ClientID,
      "X-IBM-Client-Secret" : DSP_APIKey_ClientSecret,
      "Content-type": "application/json",
      "Accept": "application/json",
      "routingInfo": "routing123",
      "traceID": "trace123",
      "transactionID": "transaction123",
      "transactionSeqNo": "trx000001"
    },
    data : {
      "commonRequestHeader": {
        "bankCode": "0130",
        "userID": "000001",
        "userIDForLogging": "test0000001",
        "applicationID": "app0000001",
        "clientID": "client0000001",
        "deviceID": "device0000001"
      },
      "inquireAccount": [
        {
          "branchNumber": branchNumber,
          "accountType": accountType,
          "accountNumber": accountNumber
        }
      ]
    }
  };
  try {
    const res = await axios.request(dspOption);
    const balance = Number(res.data.inquireResult[0].currentAmount).toLocaleString() + "円";
    return balance;
  } catch (error) {
    return false;
  }
}

exports.main = main;
