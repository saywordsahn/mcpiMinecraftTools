from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)

count = 20
for i in range(10):
    time.sleep(1)
    mc.setBlock(pos.x, pos.y, pos.z, block.SNOW_BLOCK)
    mc.setBlock(pos.x, pos.y + 1, pos.z, block.SNOW_BLOCK)
    mc.setBlock(pos.x, pos.y + 2, pos.z, block.PUMPKIN)




