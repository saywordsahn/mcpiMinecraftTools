from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from functions.teleport import teleport
import time
from Rayquaza import build_rayquaza
from TTNNTT import TNT_CANNNOOON

server = 'mc2.tokyocodingclub.com'
mc = Minecraft.create(server)

player = mc.getPlayerEntityId("TCC_10")


while True:
    for post in mc.events.pollChatPosts():
        print(post)

        if post.message.lower() == 'summon rayquazaa':
            poster_loc = mc.entity.getTilePos(post.entityId)
            build_rayquaza(poster_loc.x, poster_loc.y, poster_loc.z)

        if post.message.lower() == 'come here':
            tohma = mc.getPlayerEntityId('TCC_09')
            pos = mc.entity.getTilePos(player)
            mc.entity.setTilePos(tohma, pos.x, pos.y, pos.z)

        if post.message.lower() == 'spawn cannon':
            TNT_CANNNOOON(mc, post.entityId)

        if post.message.lower() == 'destroy':
            pos = mc.entity.getTilePos(player)
            mc.setBlocks(pos.x, pos.y, pos.z, pos. x + 25, pos.y + 25, pos.z + 25, block.AIR)