# News Feed of Trending Topics using Watson Discovery Service

[Watson Discovery News](https://www.ibm.com/watson/developercloud/discovery-news.html) is a great public data set of news articles that are analyzed by Watson on daily basis. Using Watson's Discovery Service we can query this News dataset and extract the topics from those articles and aggregate on them to get a list of the most trending topics in news. And by applying a time filter we can get the most recently topics. For each of those topics we can include a most relevant news article and convert it into a RSS feed so that it can be consumed by anyone, in any way, since RSS is a standard XML format for exchanging data.

In the [Watson Discovery News Journey](https://github.com/IBM/watson-discovery-news) that retrieves news articles from the Watson Discovery Service, we explored how we can query the Discovery Service using the nodejs SDK. Using the same SDK we can query the Discovery Service to aggregate the topics in all of the news articles and get top 20 topics using the following query:

```json
{
  "aggregations": [
    "term(enrichedTitle.entities.text,count:20)"
  ]
}
```

If we also want to include one news article for each topic we can include `top_hits(1)` in the aggregation as such:

```json
{
  "aggregations": [
    "term(enrichedTitle.entities.text,count:20).top_hits(1)"
  ]
}
```

Finally, to make the Discovery Service return the most recent topics, you can apply a filter to get topics for the past 24 hours. Here we are using a library called `moment` to subtract 24 hours from the current time:

```json
{
  "aggregations": [
    "term(enrichedTitle.entities.text,count:20).top_hits(1)"
  ],
  "filter": `blekko.chrondate>${moment().subtract(24,'h').unix()}`
}
```

Now that we have the data we can generate the RSS news feed using a node module called [rss](https://www.npmjs.com/package/rss). It is simple to use and supports a lot of options to construct a comprehensive RSS feed with custom elements if needed. For our news feed we will be sticking to the standard tags.

To construct the feed all we need to do is initialize it

```js
const feed = new RSS({
  title: `Trending Topics in News`,
  description: 'RSS feed for Trending Topics found using Watson Discovery Service'
});
```

Then iterate over the topics and extract the news story from it and create an item in the feed for it.

```js
topics.forEach(item => {
  const story = topicStory(item);
  const categories = story.enrichedTitle.taxonomy.reduce((result, categories) =>
    result.concat(categories.label.split('/').slice(1)), []);
  feed.item({
    guid: story.id,
    title: item.key,
    url: story.url,
    description: story.enrichedTitle.text,
    author: story.author,
    categories
  });
});
```

Once the news story for all of the topics have been added to the feed, we can get the XML string of the feed by calling `feed.xml()` and pass the XML string as our response in our nodejs server.

```js
res.set('Content-Type', 'text/xml').send(feed.xml());
```

Now we have a RSS feed that we can subscribe to and get push notifications via a RSS News Reader.
