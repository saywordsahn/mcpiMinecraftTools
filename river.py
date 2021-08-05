from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)


length = 20
width = 6
seg_length = 1
depth = 2
facing = '+x'

if facing == '+x':
    for x in range(length // seg_length):
        mc.setBlocks(pos.x + seg_length * x, pos.y - x, pos.z, pos.x + seg_length * x + seg_length, pos.y + depth - x, pos.z + width, block.GLASS)
        mc.setBlocks(pos.x + seg_length * x + 1, pos.y - x + 1, pos.z + 1, pos.x + seg_length * x + seg_length, pos.y + depth - x, pos.z + width - 1, block.WATER_FLOWING)
if facing == '+z':
    for x in range(length // seg_length):
        mc.setBlocks(pos.x, pos.y - x, pos.z + seg_length * x, pos.x + width, pos.y + depth - x,
                     pos.z + seg_length * x + seg_length, block.GLASS)
        mc.setBlocks(pos.x + seg_length * x + 1, pos.y - x + 1, pos.z + 1, pos.x + seg_length * x + seg_length,
                     pos.y + depth - x, pos.z + width - 1, block.WATER_FLOWING)

