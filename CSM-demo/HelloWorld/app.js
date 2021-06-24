const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!-0621-Esaki-04')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
