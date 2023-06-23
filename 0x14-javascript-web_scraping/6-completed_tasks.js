#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) =>{
if (error){
console.error(error);
	return;
}
const users = JSON.parse(body);
const user = users.filter(user => user.completed)
console.log(user);
});
