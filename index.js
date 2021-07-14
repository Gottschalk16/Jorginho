console.log('Beep beep! :)');
//cria o client que faz a ligação com o discord
const Discord = require('discord.js');
const client = new Discord.Client();
//Informa que deve carregar a informação da constante
require('dotenv').config();
client.login(process.env.TokenJorginho);
//chama a função que informa que o bot está on
client.on('ready', readyDiscord);
client.on('message', getMessage);
function readyDiscord(){
   console.log('I will do everything you want, but you will be charged!');
}
//Captura as mensagens enviadas nos canais do servidor
function getMessage(msg){
   console.log(msg.content);
   //Se a mensagem for igual a gostosa então escreve gostosa no chat
   if (msg.content === 'gostosa'){
      msg.reply('gostosa');
   }
}
