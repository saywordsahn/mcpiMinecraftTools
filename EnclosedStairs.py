from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_09")

pos = mc.entity.getTilePos(player)

block.REDSTONE = 152

blockType = block.REDSTONE
outer = block.GLASS

counter = 0
while True:
    # mc.setBlock(pos.x , pos.y - counter, pos.z - counter, blockType)
    # mc.setBlock(pos.x, pos.y - 1 , pos.z - counter, block.IRON_BLOCK)

    mc.setBlock(pos.x - 2, pos.y - counter + 2, pos.z - counter, outer)
    mc.setBlock(pos.x - 1, pos.y - counter + 2, pos.z - counter, outer)
    mc.setBlock(pos.x, pos.y - counter + 2, pos.z - counter, outer)
    mc.setBlock(pos.x + 1, pos.y - counter + 2, pos.z - counter, outer)
    mc.setBlock(pos.x + 2, pos.y - counter + 2, pos.z - counter, outer)

    mc.setBlock(pos.x - 2, pos.y - counter - 2, pos.z - counter, outer)
    mc.setBlock(pos.x - 1, pos.y - counter - 2, pos.z - counter, outer)
    mc.setBlock(pos.x, pos.y - counter - 2, pos.z - counter, outer)
    mc.setBlock(pos.x + 1, pos.y - counter - 2, pos.z - counter, outer)
    mc.setBlock(pos.x + 2, pos.y - counter - 2, pos.z - counter, outer)

    mc.setBlock(pos.x - 2, pos.y - counter + 1, pos.z - counter, outer)
    mc.setBlock(pos.x - 2, pos.y - counter, pos.z - counter, outer)
    mc.setBlock(pos.x - 2, pos.y - counter - 1, pos.z - counter, outer)

    mc.setBlock(pos.x + 2, pos.y - counter + 1, pos.z - counter, outer)
    mc.setBlock(pos.x + 2, pos.y - counter, pos.z - counter, outer)
    mc.setBlock(pos.x + 2, pos.y - counter - 1, pos.z - counter, outer)

    mc.setBlock(pos.x - 1, pos.y - counter + 1, pos.z - counter, block.AIR)
    mc.setBlock(pos.x, pos.y - counter + 1, pos.z - counter, block.AIR)
    mc.setBlock(pos.x + 1, pos.y - counter + 1, pos.z - counter, block.AIR)

    mc.setBlock(pos.x - 1, pos.y - counter, pos.z - counter, block.AIR)
    mc.setBlock(pos.x, pos.y - counter, pos.z - counter, block.AIR)
    mc.setBlock(pos.x + 1, pos.y - counter, pos.z - counter, block.AIR)

    mc.setBlock(pos.x - 1, pos.y - counter - 1 , pos.z - counter, block.AIR)
    mc.setBlock(pos.x, pos.y - counter - 1, pos.z - counter, block.AIR)
    mc.setBlock(pos.x + 1, pos.y - counter - 1, pos.z - counter, block.AIR)


    counter += 1
    time.sleep(.04)


