from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

ben = mc.getPlayerEntityId("TCC_10")
anju = mc.getPlayerEntityId("KamuiSouls")

bpos = mc.entity.getTilePos(ben)
apos = mc.entity.getTilePos(anju)

pos = bpos

# rina's castle -1314, 10, -1440
# kamui's secret fort -493, 11, -1019
#mc.entity.setTilePos(ben, apos.x, apos.y, apos.z)
mc.entity.setTilePos(anju, pos.x, pos.y, pos.z)
# mc.entity.setTilePos(ben, -493, 11, -1019)