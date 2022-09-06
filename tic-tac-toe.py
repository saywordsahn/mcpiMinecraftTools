from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc.tokyocodingclub.com")

player = mc.getPlayerEntityId("SayWordSAHN")

pos = mc.entity.getTilePos(player)

white_concrete = 251

def draw_x(x, y, z, blockType):
    mc.setBlock(x, y, z, blockType)
    mc.setBlock(x + 1, y, z + 1, blockType)
    mc.setBlock(x + 2, y, z + 2, blockType)
    mc.setBlock(x + 3, y, z + 3, blockType)
    mc.setBlock(x + 4, y, z + 4, blockType)
    mc.setBlock(x, y, z + 4, blockType)
    mc.setBlock(x + 1, y, z + 3, blockType)
    mc.setBlock(x + 3, y, z + 1, blockType)
    mc.setBlock(x + 4, y, z, blockType)

def draw_o(x, y, z, blockType):
    mc.setBlock(x, y, z, blockType)
    mc.setblock(x + 1, y, z, blockType)
    mc.setblock(x + 2, y, z, blockType)
    mc.setblock(x + 3, y, z, blockType)
    mc.setblock(x + 4, y, z, blockType)

    mc.setBlock(x, y, z + 4, blockType)
    mc.setblock(x + 1, y, z + 4, blockType)
    mc.setblock(x + 2, y, z + 4, blockType)
    mc.setblock(x + 3, y, z + 4, blockType)
    mc.setblock(x + 4, y, z + 4, blockType)



draw_x(pos.x, pos.y, pos.z, white_concrete)