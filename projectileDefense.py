from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

p1_name = 'TCC_10'
p2_name = 'TCC_03'

p1_id = mc.getPlayerEntityId(p1_name)
p2_id = mc.getPlayerEntityId(p2_name)

mc.postToChat('YOU MAY NOT SHOOT ANYONE RIGHT NOW, DO SO AND DIE')


while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        print("You hit block ({},{},{})".format(hit.pos.x, hit.pos.y, hit.pos.z))
    time.sleep(0.1)


    for proj in mc.events.pollProjectileHits():
        print(proj)
        if proj.originName == p1_name and proj.targetName == p2_name:
            mc.entity.setTilePos(p1_id, 100, -200, 100)

        if proj.originName == p2_name and proj.targetName == p1_name:
            mc.entity.setTilePos(p2_id, 100, -200, 100)
