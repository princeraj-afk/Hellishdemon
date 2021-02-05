const jokes = require('give-me-a-joke');
const color = require('colors');

jokes.getRandomDadJoke(function (e) {
    console.log(e.green);
})