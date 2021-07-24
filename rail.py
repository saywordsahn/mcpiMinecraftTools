from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)

length = 100
simple = True

# -z direction
if simple:
    print('not coded yet')
else:
    for i in range(length):
        mc.setBlocks(pos.x - 2, pos.y, pos.z - i, pos.x + 2, pos.y + 4, pos.z - i, block.AIR)
        if i % 10 == 0:
            mc.setBlock(pos.x - 1, pos.y - 1, pos.z - i, block.GLASS)
            mc.setBlock(pos.x - 1, pos.y, pos.z - i, block.TORCH_REDSTONE)
        if i % 5 == 0:
            mc.setBlock(pos.x, pos.y + 5, pos.z - i, block.GLASS)
            mc.setBlock(pos.x, pos.y + 6, pos.z - i, block.GLOWSTONE_BLOCK)
            mc.setBlock(pos.x - 4, pos.y + 1, pos.z - i, block.GLOWSTONE_BLOCK)
            mc.setBlock(pos.x + 4, pos.y + 1, pos.z - i, block.GLOWSTONE_BLOCK)
            mc.setBlock(pos.x - 3, pos.y + 1, pos.z - i, block.GLASS)
            mc.setBlock(pos.x + 3, pos.y + 1, pos.z - i, block.GLASS)
        mc.setBlock(pos.x, pos.y - 1, pos.z - i, block.GLASS)
        mc.setBlock(pos.x, pos.y, pos.z - i, block.RAIL_POWERED)




