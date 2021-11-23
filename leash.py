from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

p1 = 'TCC_04'

ben = mc.getPlayerEntityId(p1)
anju = mc.getPlayerEntityId("TCC_10")

bpos = mc.entity.getTilePos(ben)
apos = mc.entity.getTilePos(anju)

pos = bpos

# mc.entity.setTilePos(anju, pos.x, pos.y, pos.z)
while True:
    bpos = mc.entity.getTilePos(ben)
    apos = mc.entity.getTilePos(anju)

    x = pow(apos.x - bpos.x, 2)
    y = pow(apos.y - bpos.y, 2)
    z = pow(apos.z - bpos.z, 2)

    dist = pow(x + y + z, .5)
    mc.postToChat('Distance from ' + p1 + ': ' + str(dist))

    if dist > 100:
        mc.postToChat('You''re too far away, come back')
        mc.entity.setTilePos(anju, bpos.x, bpos.y, bpos.z)


    time.sleep(1)




# rina's castle -1314, 10, -1440
# kamui's secret fort -493, 11, -1019
#mc.entity.setTilePos(ben, apos.x, apos.y, apos.z)
# mc.entity.setTilePos(ben, -493, 11, -1019)