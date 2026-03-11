var express = require('express');
var app = express();

app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader('Access-Control-Allow-Methods', '*');
  res.setHeader("Access-Control-Allow-Headers", "*");
  next();
});

app.use('/', express.static(__dirname));
app.get('/', (req, res) => res.sendFile(__dirname + '/index.html'));

var server = app.listen(8080, function () {
  var host = "127.0.0.1"
  var port = "8080"

  console.log('my app is listening at http://%s:%s', host, port);
});
