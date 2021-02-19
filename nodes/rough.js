const jokes = require('give-me-a-joke')
const colors = require('colours')

jokes.getRandomDadJoke(joke => console.log(joke.rainbow));