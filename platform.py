from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_14")

pos = mc.entity.getTilePos(player)

x = pos.x
y = pos.y
z = pos.z

length = 30
width = 6
blockType = block.TNT
# 70 is pressures


for i in range(length):
    for j in range(width):
        if i % 2 == 0:
            mc.setBlock(x + i, y, z + j, blockType)
            mc.setBlock(x + i, y + 1, z + j, block.SAND)
            time.sleep(.1)
            mc.setBlock(x + i, y + 2, z + j, 70)
