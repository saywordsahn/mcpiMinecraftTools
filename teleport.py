from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

ben = mc.getPlayerEntityId("TCC_10")
rina = mc.getPlayerEntityId("KamuiLinkPro")

bpos = mc.entity.getTilePos(ben)
rpos = mc.entity.getTilePos(rina)

pos = bpos


# rina's castle -1314, 10, -1440
mc.entity.setTilePos(rina, pos.x, pos.y, pos.z)
# mc.entity.setTilePos(ben, pos.x, pos.y, pos.z)