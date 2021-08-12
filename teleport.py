from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

ben = mc.getPlayerEntityId("TCC_04")
kamui = mc.getPlayerEntityId("KamuiLinkPro")

bpos = mc.entity.getTilePos(ben)
kpos = mc.entity.getTilePos(kamui)

pos = kpos
print(pos)

#kamui's secret base -516, 76, -1026
# rina's castle -1314, 10, -1440
# mc.entity.setTilePos(ben,-1314, 10, -1440)
mc.entity.setTilePos(ben, pos.x, pos.y, pos.z)