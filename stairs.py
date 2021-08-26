from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)


facing = '+z'

block.REDSTONE = 152

length = 50
blockType = block.TNT


if facing == '+z':
    for i in range(length):
        mc.setBlock(pos.x, pos.y - i, pos.z + i, blockType)
elif facing == '-z':
    for i in range(length):
        mc.setBlock(pos.x, pos.y - i, pos.z - i , blockType)

else:
    for i in range(length):
        mc.setBlock(pos.x + i, pos.y + i, pos.z, blockType)

    for i in range(length):
        mc.setBlock(pos.x + i, pos.y + i + 1, pos.z, block.RAIL_POWERED )


