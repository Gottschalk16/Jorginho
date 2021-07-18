module.exports = function (msg, args){
   msg.channel.send(`${msg.guild.name} possui ${msg.guild.memberCount} membros!`);
}