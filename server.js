const express = require('express')
const serveStatic = require("serve-static")
const path = require('path')
const fetch = require('node-fetch')
const app = express()

app.use(serveStatic(path.join(__dirname, 'dist')))

const port = process.env.PORT || 80;
const DATA_URI = process.env.DATA_URI || 'https://eventqueue.herokuapp.com/events'

app.get('/events', (req, res) => {
  console.log('Events requested')
  console.log(`Data URI: ${DATA_URI}`)
  fetch(DATA_URI, {method: 'GET'})
    .then(response => response.json())
    .then(json => {
      res.send(json)
    });
});

app.listen(port)
console.log("Server started at port " + port)
