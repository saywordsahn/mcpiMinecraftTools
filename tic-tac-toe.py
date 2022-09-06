from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc.tokyocodingclub.com")

player = mc.getPlayerEntityId("SayWordSAHN")

pos = mc.entity.getTilePos(player)

white_concrete = 251