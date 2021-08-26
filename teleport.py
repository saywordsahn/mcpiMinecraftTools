from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

ben = mc.getPlayerEntityId("TCC_05")
anju = mc.getPlayerEntityId("KamuiLinkPro")

bpos = mc.entity.getTilePos(ben)
apos = mc.entity.getTilePos(anju)

pos = apos

# rina's castle -1314, 10, -1440
# kamui's secret fort -493, 11, -1019
mc.entity.setTilePos(ben, pos.x, pos.y, pos.z)
# mc.entity.setTilePos(anju, -1314, 10, -1440)
# mc.entity.setTilePos(ben, -1359, 130, -1500)