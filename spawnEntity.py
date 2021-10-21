from mcpi.minecraft import Minecraft
from mcpi import entity
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)


number = 5
creature = 20
for i in range(number):
    mc.spawnEntity( pos.x, pos.y, pos.z, creature)
    time.sleep(2)
#
# while True:
#     for entity in mc.getEntities():
#         print(entity)
#         if entity[2] == 'ZOMBIE':
#             mc.entity.setTilePos(entity[0], pos.x, pos.y, pos.z)
#             print(entity)
#             time.sleep(.1)