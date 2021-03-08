# Promises over Callbacks

Promises are a great feature in Javascript that allows you to avoid [callback hell](http://callbackhell.com), especially when you need to wait on a response from multiple API requests which are asynchronous. The ability to chain Promises and wait for one async request to finish before performing another async request, or waiting for multiple async requests to finish before moving forward can easily be solved in an elegant way using Promises.

## The Problem

In the developer journey of making a [Discovery News Search Slack Bot App](https://github.com/IBM/watson-discovery-news) using the [Discovery node SDK](https://github.com/watson-developer-cloud/node-sdk), I noticed the APIs relied heavily on the callbacks instead of promises, where the callback gets passed `error` as the first argument and `response` as the second. We then need to check if `error` is not `undefined` or `null` before we can use the `response`.

This pattern can result in a lot of nested callbacks and a huge callback function body since we need to handle both success and error states, all making the code harder to read and follow.

```js
const DiscoveryV1 = require('watson-developer-cloud/discovery/v1');

// Initialize the Discovery service with credentials from Bluemix
const discovery = new DiscoveryV1({
  username: '<username>',
  password: '<password>',
  version_date: DiscoveryV1.VERSION_DATE_2017_04_27
});

// Get all of the environments
discovery.getEnvironments({}, (error, response) => {
  if (error) {
    console.error(error);
  } else {

    // Find the environemnt id for News collection
    const news_environment_id = response.environments
      .find(env => env.read_only == true).environment_id;

    // Get the New collection ID using the environment
    discovery.getCollections({ environment_id: news_environment_id }, (error, response) => {
      if (error) {
        console.error(error);
      } else {
        const news_collection_id = response.collections[0].collection_id;

        // Now we can query discovery news collection
        discovery.query({
          environment_id: news_environment_id,
          collection_id: news_collection_id
          query: 'my_query'
        }, (error, response) => {
          if (error) {
            console.error(error);
          } else {
            // By the time we get the response we have 6 levels of nesting
            console.log(response);
          }
        });
      }
    });
  })
});
```

## Promises and bluebird to the Rescue

To fix this anti-pattern, we can use Javascript Promises along with a library called [bluebird](http://bluebirdjs.com/) which provides a higher level of abstraction around promises. The library is great in that it provides us with ability to wait on multiple promises before firing a callback, or helps us wrap callback based API's that get passed error and success response as arguments into Promises that can be chain instead. Below is the same code as above but it wraps some of the functions in the Discovery API to return promises using the `promisify` factory method.

```js
const DiscoveryV1 = require('watson-developer-cloud/discovery/v1');

// Initialize the Discovery service
const discovery = new DiscoveryV1({
  username: '<username>',
  password: '<password>',
  version_date: DiscoveryV1.VERSION_DATE_2017_04_27
});

// Promisify the API using Bluebird's promisify factory function
discovery.getEnvironments = Promise.promisify(discovery.getEnvironments);
discovery.getCollections = Promise.promisify(discovery.getCollections);
discovery.query = Promise.promisify(discovery.query);

let environmentId;
discovery.getEnvironments({})
.then(response => { // Response for environment gets passed in the then block
  environmentId = response.environments
    .find(env => env.read_only == true).environment_id;

  // Returning a promise inside the then block will cause
  // the next `then` block to fire when the discovery.getCollection
  // async request finishes and passes the result of getCollection
  // as the first argument to the callback in the next `then` function
  return discovery.getCollections({ environment_id: environmentId });
})

// This then block will get called when the getCollection async request
// finished and passed the result in the response
.then(response => {
  collectionId = response.collections[0].collection_id;

  // Now we can run a query against our discovery service
  return discovery.query({
      environment_id: news_environment_id,
      collection_id: news_collection_id
      query: 'my_query'
    })
})

// The response of the discovery query gets passed to this
// then block
.then(response => console.log(response));

// Any errors that occur anywhere in this flow gets caught by this catch
// block and can be logged and handled independently from the success cases above
.catch(error => console.error(error));
```

## Less nesting and straightforward data flow

As seen in the `promisified` code, we have only one level of nesting versus six levels of nesting. Another benefit is separation of the success and error workflows, making our code easy to follow and debug.

Another benefit of using promises is that if you return a promise inside of a `then` block, it waits for that promise to resolve before invoking the next `then` block with the response containing the resolved value of the promise that was returned:

```js
.then(response => {
  //...

  // Returning a promise results in the next chained
  // then callback function to be called when this promise resolve
  return discovery.query({
      environment_id: news_environment_id,
      collection_id: news_collection_id
      query: 'my_query'
    })
})

// The response of the discovery query gets passed to this
// then block
.then(response => console.log(response));
```

## Conclusion

Use promises over callbacks, and if the API you are using does not support it, use a library like `bluebird` which can help you wrap the API to return a promise instead.

I hope this helps simplify your use of the Discovery API and shows you an example of where Javascript Promises can be used to simplify the workflow in your code.
