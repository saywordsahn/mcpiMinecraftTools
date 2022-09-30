from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc.tokyocodingclub.com")

player = mc.getPlayerEntityId("SayWordSAHN")

pos = mc.entity.getTilePos(player)

white_concrete = 155
hopper = 154
air = 0
chest = 54
cactus = 81
sand = 12
fence = 85

mc.setBlocks(pos.x, pos.y, pos.z, pos.x + 10, pos.y + 1, pos.z + 10, white_concrete)
mc.setBlock(pos.x + 5, pos.y, pos.z + 5, 0)
mc.setBlock(pos.x + 5, pos.y - 1, pos.z + 5, hopper)
mc.setBlock(pos.x + 5, pos.y - 2, pos.z + 5, chest)
mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x + 10 - 1, pos.y + 1, pos.z + 10 - 1, air)

for i in range(0, 8, 2):
    mc.setBlock(pos.x + i + 2, pos.y + 3, pos.z + 3, fence)

for i in range(0, 8, 2):
    mc.setBlock(pos.x + i + 2, pos.y + 3, pos.z + 7, fence)

for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        mc.setBlock(pos.x + i + 2, pos.y + 1, pos.z + j + 2, sand)
        mc.setBlock(pos.x + i + 2, pos.y + 2, pos.z + j + 2, cactus)

mc.setBlock(pos.x + 1, pos.y + 1, pos.z + 1, block.WATER_FLOWING)
mc.setBlock(pos.x + 1, pos.y + 1, pos.z + 9, block.WATER_FLOWING)
mc.setBlock(pos.x + 9, pos.y + 1, pos.z + 1, block.WATER_FLOWING)
mc.setBlock(pos.x + 9, pos.y + 1, pos.z + 9, block.WATER_FLOWING)
