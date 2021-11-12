from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_03")
attacker = mc.getPlayerEntityId('TCC_10')

pos = mc.entity.getTilePos(player)
attackerPos = mc.entity.getTilePos(attacker)

mc.postToChat('A player is immune to the void.')

while True:
    pos = mc.entity.getTilePos(player)

    if pos.y <= 0:
        mc.entity.setTilePos(player, attackerPos.x, attackerPos.y, attackerPos.z)

    time.sleep(.5)