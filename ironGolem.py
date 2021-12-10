from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_08")

pos = mc.entity.getTilePos(player)

def spawn_iron_golem(x, y, z):
    mc.setBlock(x, y, z, block.IRON_BLOCK)
    mc.setBlock(x, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x + 1, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x - 1, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x, y + 2, z, block.PUMPKIN)


count = 10
for i in range(count):
    time.sleep(1)
    spawn_iron_golem(pos.x, pos.y, pos.z)


