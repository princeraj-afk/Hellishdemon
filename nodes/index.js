const jokes = require('give-me-a-joke');
const color = require('colors');

// jokes.getRandomDadJoke(function (e) {
//     console.log(e.gr);
// })
const fig = require('figlet')

fig("bitch, please!", function (err, data) {
    if (err) {
        console.log("Something went wrong");
        return;
    }
    console.log(data.cyan);
})