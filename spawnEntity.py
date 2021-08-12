from mcpi.minecraft import Minecraft
from mcpi import entity
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_08")

pos = mc.entity.getTilePos(player)


number = 5
creature = entity.ZOMBIE
for i in range(number):
    mc.spawnEntity(pos.x, pos.y, pos.z, creature)


#
# for entity in mc.getEntities():
#     if entity[2] == 'CREEPER' or entity[2] == 'SPIDER' or entity[2] == 'SKELETON':
#         cpos = mc.entity.getTilePos(entity[0])
#         distance_from_player = pow(pow(pos.x - cpos.x, 2) + pow(pos.y - cpos.y, 2) + pow(pos.z - cpos.z, 2), .5)
#
#         if distance_from_player < 50:
#             mc.entity.setTilePos(entity[0], cpos.x, -100, cpos.z)
#             print(entity)
#             print(distance_from_player)
#         time.sleep(.1)