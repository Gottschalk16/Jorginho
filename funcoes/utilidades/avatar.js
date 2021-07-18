module.exports = function (msg, args){
   if (!msg.mentions.users.size){
      return msg.channel.send(`${msg.author.displayAvatarURL({dynamic: true})}`);
   }
   const avatarList = msg.mentions.users.map(user => {
      return `${user.displayAvatarURL({dynamic: true})}`;
   });
   return msg.channel.send(avatarList);
}