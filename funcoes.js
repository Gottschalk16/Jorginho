//constantes
const gif = require('./funcoes/gif.js');
const ping = require ('./funcoes/ping.js');
const server = require ('./funcoes/infoserver.js');
const user = require ('./funcoes/user-info.js');
const banir = require ('./funcoes/banimento.js');
const avatar = require ('./funcoes/avatar.js');
const commands = { gif, ping, server, user, banir, avatar };

module.exports = async function (msg){
   let tokens = msg.content.split(" ");
   let command = tokens.shift();
   if (command.charAt(0) === '!'){
      command = command.substring(1);
      commands[command](msg, tokens);
   }
}