'use strict';

/**
* Dan,
* it was a pleasure working together.
* You know what you're doing and you're doing it well!
* Enjoy as much as you can in the army, and make the best out of it.
* I'm sure we will all hear about you in the future.
* Here's something fun to pass the time.
* So long,
* Itay Kimia
*/

const childProcess = require('child_process');

const fun = [
    'http://xkcd.com/',
    'http://www.smbc-comics.com/',
    'http://explosm.net/',
    'https://www.penny-arcade.com/comic',
    'http://dilbert.com/',
    'http://www.userfriendly.org/',
    'http://www.vgcats.com/comics',
    'http://tech.forter.com/'
];

function command() {
    return {darwin: 'open', win32: 'start'}[process.platform] || 'xdg-open';
}

function showSomeFun() {
    const chosen = fun[Math.floor(Math.random() * fun.length)];
    console.log(`Hi Dan!\nOpening ${chosen}\nHave fun!`);
    setTimeout(() => childProcess.exec(`${command()} ${chosen}`), 500);
}

showSomeFun();
