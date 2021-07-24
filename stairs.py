from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)

length = 10
blockType = block.GLASS


for i in range(length):
    mc.setBlock(pos.x + i, pos.y + i, pos.z, blockType)

for i in range(length):
    mc.setBlock(pos.x + i, pos.y + i + 1, pos.z, block.RAIL_POWERED )


