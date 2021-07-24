from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)


length = 20
width = 20
height = 8
blockType = block.STAINED_GLASS


