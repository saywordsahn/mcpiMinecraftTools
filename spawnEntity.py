from mcpi.minecraft import Minecraft
from mcpi import entity
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)


number = 30
creature = entity.PIG
# for i in range(number):
#     mc.spawnEntity(creature, pos.x, pos.y, pos.z)
#     mc.spawnEntity(entity.BOAT, pos.x, pos.y, pos.z)
#     time.sleep(2)


for entity in mc.getEntities():
    if entity[2] == 'CREEPER':
        mc.entity.setTilePos(entity[0], pos.x, pos.y, pos.z)
        print(entity)
        time.sleep(.1)