//constantes
const fetch = require('node-fetch');

module.exports = async function (msg){
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