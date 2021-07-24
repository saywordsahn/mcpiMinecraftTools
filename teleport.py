from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

ben = mc.getPlayerEntityId("TCC_10")
rina = mc.getPlayerEntityId("TCC_09")

bpos = mc.entity.getTilePos(ben)
rpos = mc.entity.getTilePos(rina)

pos = bpos
print(pos)


# rina's castle -1314, 10, -1440
# mc.entity.setTilePos(ben,-1314, 10, -1440)
mc.entity.setTilePos(rina, pos.x, pos.y, pos.z)