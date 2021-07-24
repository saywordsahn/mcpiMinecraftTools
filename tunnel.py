from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)

length = 80
height = 10
width = 8
facing = '-z'
boarderBlock = block.GLASS
boarder = True
incline = True

# -z direction
for i in range(length):
    if boarder:
        mc.setBlocks(pos.x, pos.y + i, pos.z - i, pos.x + width, pos.y + i + height, pos.z - i, boarderBlock)
        mc.setBlocks(pos.x + 1, pos.y + i + 1, pos.z - i, pos.x + width - 1, pos.y + i + height - 1, pos.z - i, block.AIR)






