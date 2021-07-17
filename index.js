console.log('Beep beep! :)');
const fetch = require('node-fetch');
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
//Captura as mensagens enviadas nos canais do servidor e realiza ações de acordo com o comando
async function getMessage(msg){
   let tokens = msg.content.split(" ");
   console.log(msg.content);
   //Se a mensagem for igual a gostosa então escreve gostosa no chat
   if (tokens [0] === 'gostosa'){
      msg.reply('gostosa');
   }
   if (tokens [0] === '!gif'){
      let keywords = 'Jorginho';
      if (tokens.length > 1){
         keywords = tokens.slice(1, tokens.length).join(" ");
      }
      let url = `https://api.tenor.com/v1/search?q=` + keywords +`&key=` + process.env.TokenTenor + `&ContentFillter=high`;
      console.log(url);
      let response = await fetch(url);
      let json = await response.json();
      const index = Math.floor(Math.random() * json.results.length);
      console.log(json);
      msg.channel.send(json.results[index].url);
      msg.channel.send('Gif from Tenor: ' + keywords);
   }
}
