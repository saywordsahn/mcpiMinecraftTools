from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from functions.teleport import teleport
import time

server = 'mc2.tokyocodingclub.com'
mc = Minecraft.create(server)

player = mc.getPlayerEntityId("TCC_10")
pos = mc.entity.getTilePos(player)


while True:
    for post in mc.events.pollChatPosts():
        if post.entityId == player:
            args = post.message.split()

            if args[0].lower() == 'repeat':
                new_list = args[1:]
                mc.postToChat(' '.join(new_list))
            elif args[0].log() == 'teleport':
                if args[1].lower() == 'me':
                    teleport(server, player, args[3].lower())
                else:
                    teleport(server, args[1], player)
