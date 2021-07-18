require('dotenv').config();
const fetch = require('node-fetch');

module.exports = async function (msg, args){
   let keywords = 'Jorginho';
   if (args.length > 0){
      keywords = args.join(" ");
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