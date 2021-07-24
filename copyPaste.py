from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)


length = 20
width = 20
height = 2

blockInfo = []

# block = mc.getBlock(pos.x, pos.y - 1, pos.z)
print(block)

for i in range(length):
    x = []
    for j in range(height):
        y = []
        for k in range(width):
            block = mc.getBlock(pos.x, pos.y, pos.z)
            print(block)

