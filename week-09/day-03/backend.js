'use strict';

var express = require('express');

var app = express();
app.use('/assets', express.static('./assets'));
express.json.type = "application/json";

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(req, res){
    if(req.query.input === undefined){
        res.json({error : "Please provide an input!"});
    } else {
        res.json({received : req.query.input, result : req.query.input*2})
    }
});

app.get('/greeter', function(req, res){
    if(req.query.name === undefined){
        res.json({error : "Please provide a name!"});
    } else if(req.query.title === undefined){
        res.json({error : "Please provide a title!"});
    } else {
        res.json({welcome_message : "Oh, hi there " 
        + req.query.name + ", my dear " 
        + req.query.title + "!"})
    }
});

app.get('/appenda/:appendable', function(req, res){
    res.json({appended : req.params.appendable + "a"})
});


app.listen(8080);