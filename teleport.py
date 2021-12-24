from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

ben = mc.getPlayerEntityId("TCC_10")
anju = mc.getPlayerEntityId('TCC_09')

bpos = mc.entity.getTilePos(ben)
apos = mc.entity.getTilePos(anju)

pos = bpos

mc.entity.setTilePos(ben, apos.x, apos.y, apos.z)






# tohmas house -2888, 63, 6351
# rina's castle -1314, 10, -1440
# kamui's secret fort -493, 11, -1019
#mc.entity.setTilePos(ben, apos.x, apos.y, apos.z)
# mc.entity.setTilePos(ben, -493, 11, -1019)