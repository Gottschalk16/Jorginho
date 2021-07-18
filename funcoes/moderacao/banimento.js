module.exports = function (msg, args){
   if (!msg.mentions.users.size){
      return msg.reply('Você deve marcar um usuário para explusá-lo!');
   }
   const taggedUser = msg.mentions.users.first();
   msg.channel.send(`Você deseja banir ${taggedUser.username} ?`);
}