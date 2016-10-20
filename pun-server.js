var express = require('express');
//var apicache = require('apicache').options({ debug: true }).middleware;
var app = express();
var spawn = require('child_process').spawn;
var path = require('path');

var fs = require('fs');
var settings = JSON.parse(fs.readFileSync(path.resolve(__dirname, './settings.json'), 'utf8'));

var punScript = path.resolve(__dirname, './pun.py');

function run(command, args, callback) {
  console.log(command, args);
  var child = spawn(command, args);
  var response = '';
  var error = '';
  child.stdout.on('data', function(buffer) {
    response += buffer.toString();
  });
  child.stderr.on('data', function(buffer) {
    error += buffer.toString();
  });
  child.on('close', function(code) {
    if (code === 0) {
      callback(response);
    } else {
      callback(null, error);
    }
  });
}

console.log('registering /');
app.get('/' /*, apicache('5 minutes')*/, function(req, res) {
  console.log('GET ' + req.originalUrl);
  if (settings.origin) {
    res.setHeader('Access-Control-Allow-Origin', settings.origin);
  }

  res.set({
    'Content-Type': 'application/json'
  });

  run(punScript, [], function(pun, err) {
    if (err) {
      err = err.trim();
      console.error(err);
      res.status(500);
      res.send(req.accepts('application/json') ? {"error": err} : err);
      return;
    }

    if (pun) {
      pun = pun.trim();
    }

    res.status(200);
    res.send(req.accepts('application/json') ? {"pun": pun} : pun);
  });
});

var port = settings.port;
app.listen(port);
console.log('listening on ' + port);

