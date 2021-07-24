from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

ben = mc.getPlayerEntityId("TCC_10")
bpos = mc.entity.getTilePos(ben)
print(bpos)
mc.postToChat("Underwater zoo is at: " + str(bpos))

# Vec3(-1307,8,-1081)