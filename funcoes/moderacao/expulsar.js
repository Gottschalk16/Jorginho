module.exports = function (msg, args){
   if (!msg.mentions.users.size){
      msg.channel.send(console.log);
      return msg.reply('Você deve marcar um usuário para explusá-lo!');
   }
   const taggedUser = msg.mentions.users.first();
   if (member.hasPermission('ADMINISTRATOR') || members.hasPermission('KICK_MEMBERS')){
      const target = mentions.users.first();
      if (target) {
         const targetMember = msg.guild.members.cache.get(target.id);
         targetMember.kick();
         msg.channel.sen('Usuário expulso')
      }
      console.log(target);
   }else {
      msg.channel.send('Você não tem permissão para usar o comando de expulsar.');
   }
}