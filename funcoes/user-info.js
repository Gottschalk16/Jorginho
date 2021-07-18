module.exports = function (msg, args){
   msg.channel.send(`Seu nick: ${msg.author.username} \nSeu ID: ${msg.author.id}`);
}
