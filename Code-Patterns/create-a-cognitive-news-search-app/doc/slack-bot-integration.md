# Slack Bot Integration

It has never been a more exciting time to create a chatbot. With the rise of AI based APIs from multiple companies such as [IBM Watson](https://www.ibm.com/watson/developercloud/conversation.html), and thanks to great SDK's like [Botkit](https://www.botkit.ai), it is easy to create your own chatbot to respond to FAQ's from your customer, automate responses to help reduce customer service staff, help automate deployments at your company, or have it to do mundane tasks on your behalf.

In the developer journey to create a [Watson Discovery News Slackbot](https://github.com/IBM/watson-discovery-news) to serve news articles using Watson Discovery API, we are using `Botkit` to create a chatbot which acts as a middleman to facilitate queries to the Watson Discovery Service via conversation with the user from Slack.

## Slack's RTM API

Slack has multiple API's to create bots and commands, but in the journey we decided to use Slack's Real Time Messaging (RTM) API. The API lets you create a connection with Slack and any request to the bot user, or to the bot directly, or from within a slack channel in which the bot is a member, gets sent to the server that starts up the connection, with Slack using the bot token as a means to authenticate.

Botkit provides a great abstraction layer over this Slack API and lets you easily create a slack bot in few minutes in a nodejs application. Below is the code you need to estabilish a connection with Slack and make your bot user active on Slack.

```js
const Botkit = require('botkit');
const controller = Botkit.slackbot();
const bot = controller.spawn({
  token: '<SLACK_BOT_TOKEN>'
}).startRTM();
```

## How to listen to messages and respond

Listening for messages is as easy as specifying what keywords you want to listen to. You also need to specify whether those keywords are directed directly to the bot user or in the slack channel. Below we are listening for a direct message or mention of the bot user in a slack channel and respond with a text reply of `Hello`.

```js
controller.hears(['hello', 'hi'], 'direct_message,direct_mention,mention', function(bot, message) {
  bot.reply(message, 'Hello');
});
```

## Having a conversation

In the developer journey, we are trying to make a bot that feels realistic by having it start a conversation with the user to figure out what news the user is interested in. We can do so by starting a conversation as such:

```js
bot.startConversation(message, function(err, convo) {
  convo.say('Hi there!');
  convo.ask('What news are you interested in?', function(response, convo) {
    // Response passed here
  });
});
```

Calling `convo.next();` inside the ask callback function moves the bot forward in conversation until finally `convo.on('end', callback)` is called. You can also end the conversation at any time by calling `convo.stop()` or repeat a conversation with `convo.repeat()`.

Inside the callback for the `end` event, the callback gets passed the status of the conversation which can either be marked as `completed` to mark the the end of the conversation without being stopped anywhere in between. Here you can make a network request to the Discovery Service to get the list of articles and reply back to the user with links to the news articles for that topic.

![Chatting with Slackbot](https://raw.githubusercontent.com/IBM/watson-discovery-news/master/doc/source/images/slack-3.png)
