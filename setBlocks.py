from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)


length = 6
width = 6
height = 0
blockType = block.GRASS

facing = '-z'
hollow = False
aquarium = False



if facing == '+x':
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x + length, pos.y + height, pos.z + width, blockType)
    if hollow:
        mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x + length - 1, pos.y + height - 1, pos.z + width - 1, 0)

if facing == '-x':
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x - length, pos.y + height, pos.z - width, blockType)
    if hollow:
        mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1, pos.x - length + 1, pos.y + height - 1, pos.z - width + 1, 0)

    if aquarium:
        mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1, pos.x - length + 1, pos.y + height - 1, pos.z - width + 1,
                     block.WATER)
        mc.setBlocks(pos.x - 2, pos.y + 2, pos.z - 2, pos.x - length + 2, pos.y + height - 2, pos.z - width + 2,
                     blockType)
        mc.setBlocks(pos.x - 3, pos.y + 3, pos.z - 3, pos.x - length + 3, pos.y + height - 3, pos.z - width + 3,
                     block.AIR)


if facing == '-z':
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x + width, pos.y + height, pos.z - length, blockType)
    if hollow:
        mc.setBlocks(pos.x + 1, pos.y + 1, pos.z - 1, pos.x + width - 1, pos.y + height - 1, pos.z - length + 1, 0)

if facing == '+z':
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x - width, pos.y + height, pos.z + length, blockType)
    if hollow:
        mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1, pos.x - width + 1, pos.y + height - 1, pos.z + length - 1, 0)

