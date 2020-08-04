const express = require('express');
const serveStatic = require("serve-static")
const path = require('path');
const fetch = require('node-fetch');
const app = express();

app.use(serveStatic(path.join(__dirname, 'dist')));

const port = process.env.PORT || 80;
const DATA_URI = process.env.DATA_URI || 'https://eventqueue.herokuapp.com/events';
const HASH_URI = process.env.HASH_URI || 'https://eventqueue.herokuapp.com/hash';

app.get('/events', (req, res) => {
  fetch(DATA_URI, {method: 'GET'}).
    then(res => res.json()).
    then((json) => {
      res.send(json);
    });
});

app.get('/hash', (req, res) => {
  fetch(`${HASH_URI}?previous=${req.query.previous}&data=${req.query.data}` , {method: 'GET'}).
    then(res => res.json()).
    then((json) => {
      res.send(json);
    });
});

app.get('/*', (req, res) => {
  res.sendFile(path.join(__dirname, './dist', 'index.html'))
});

app.listen(port);
console.log("Server started at port " + port);
