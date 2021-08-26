from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_05")

pos = mc.entity.getTilePos(player)

head = True
foot = False
blockType = block.GLOWING_OBSIDIAN

while True:
    mc.setBlock(pos.x, pos.y + 3, pos.z, blockType)
    pos = mc.entity.getTilePos(player)
    time.sleep(.2)
