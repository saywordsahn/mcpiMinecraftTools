from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_04")

pos = mc.entity.getTilePos(player)


length = 5
width = 6
height = 5

blockInfo = []

# block = mc.getBlock(pos.x, pos.y - 1, pos.z)
print(block)

for i in range(length):
    slice = []
    for j in range(height):
        y = []
        for k in range(width):
            block = mc.getBlock(pos.x + i, pos.y + j, pos.z + k)
            y.append(block)
        slice.append(y)
    blockInfo.append(slice)
print(blockInfo)