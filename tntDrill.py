from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)



blockType = block.TNT


counter = 0
while True:
    mc.setBlock(pos.x + counter, pos.y, pos.z, blockType)
    mc.setBlock(pos.x + counter, pos.y - 1, pos.z, block.IRON_BLOCK)
    counter += 1
    time.sleep(.04)