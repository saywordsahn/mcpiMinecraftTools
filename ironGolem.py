from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_08")

pos = mc.entity.getTilePos(player)

count = 10
for i in range(count):
    time.sleep(1)
    mc.setBlock(pos.x, pos.y, pos.z, block.IRON_BLOCK)
    mc.setBlock(pos.x, pos.y + 1, pos.z, block.IRON_BLOCK)
    mc.setBlock(pos.x + 1, pos.y + 1, pos.z, block.IRON_BLOCK)
    mc.setBlock(pos.x - 1, pos.y + 1, pos.z, block.IRON_BLOCK)
    mc.setBlock(pos.x, pos.y + 2, pos.z, block.PUMPKIN)


