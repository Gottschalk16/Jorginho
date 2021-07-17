//cria o client que faz a ligação com o discord
const Discord = require('discord.js');
const client = new Discord.Client();
const commandHandler = require("./funcoes")
//Informa que deve carregar a informação da constante
require('dotenv').config();
client.login(process.env.TokenJorginho);
//chama a função que informa que o bot está on
client.on('ready', readyDiscord);
client.on('message', commandHandler);
function readyDiscord(){
   console.log('I will do everything you want, but you will be charged!');
}