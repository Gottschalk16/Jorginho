//constantes
const gif = require('./funcoes/diversao/gif.js');
const ping = require ('./funcoes/diversao/ping.js');
const server = require ('./funcoes/utilidades/infoserver.js');
const user = require ('./funcoes/utilidades/user-info.js');
const banir = require ('./funcoes/moderacao/banimento.js');
const avatar = require ('./funcoes/utilidades/avatar.js');
const expulsar = require ('./funcoes/utilidades/expulsar.js');
const commands = { gif, ping, server, user, banir, avatar, expulsar };

module.exports = async function (msg){
   let tokens = msg.content.split(" ");
   let command = tokens.shift();
   if (command.charAt(0) === '!'){
      command = command.substring(1);
      commands[command](msg, tokens);
   }
}