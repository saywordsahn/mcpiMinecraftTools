from mcpi.minecraft import Minecraft
import time
from mcpi import block
mc = Minecraft.create('mc2.tokyocodingclub.com')

player = mc.getPlayerEntityId('TCC_04')


while True:
    x, y, z = mc.entity.getTilePos(player)

    mc.setBlock(x, y, z, block.TNT)
    mc.setBlock(x, y + 1, z, block.TORCH_REDSTONE)

    time.sleep(.5)







