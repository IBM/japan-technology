const express = require('express');
const { Configuration, OpenAIApi } = require("openai");
const DiscoveryV2 = require('ibm-watson/discovery/v2');
const { IamAuthenticator } = require('ibm-watson/auth');
require('dotenv').config();
const app = express();
app.use(express.json())
app.use(express.urlencoded({ extended: true }));
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./openapi.json');
const resourceCount = 3
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

const port = 8080;
const configuration = new Configuration({
    apiKey: process.env.GPT_API_KEY,
});
const discovery = new DiscoveryV2({
    version: '2023-03-31',
    authenticator: new IamAuthenticator({
        apikey: process.env.DISCOVERY_API_KEY,
    }),
    serviceUrl: process.env.DISCOVERY_SERVICE_URL,
});

const openai = new OpenAIApi(configuration);

const getDiscoveryData = async (query) => {
    const params = {
        projectId: process.env.DISCOVERY_PROJECT_ID,
        naturalLanguageQuery: query,
    };
    try {
        const _discoveryDoc = await discovery.query(params)
        const discoveryDoc = _discoveryDoc.result.results.map((doc) => doc.text)
        return discoveryDoc
    } catch (error){
        console.log('error:', err);
    }   
}

app.post('/chat_discovery', async (req, res) => {
    const query = req.body.content
    console.log(query)
    results = await getDiscoveryData(query)

    try {
        let discovery_doc = ''
        for(const j of results) {
            if (discovery_doc.length + j[0].length < 2500) {
                console.log("j:" + j)
                discovery_doc = discovery_doc + j[0];
            } 
        }
        console.log(discovery_doc)
        let prompt = query + 'という質問が来ています。社内文書を検索したところ、質問に対する回答を、ヒットしたドキュメントの要約を加えながら作成してください。文中になかったら、要約はしなくていいので回答をください。ドキュメント: ' + discovery_doc;
            const completion = await openai.createChatCompletion({
                model: "gpt-3.5-turbo-0301",
                messages: [{ role: "user", content: prompt }],
            });
            const chatResponse = completion.data.choices[0].message;
            res.json({content:chatResponse.content});
    } catch (error) {
        console.error(error);
        res.status(500).send('Error occurred while communicating with ChatGPT API');
    }

});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});