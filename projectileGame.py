from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

p1_name = 'TCC_10'
p2_name = 'TCC_05'

p1_id = mc.getPlayerEntityId(p1_name)
p2_id = mc.getPlayerEntityId(p2_name)

p1_health = 10
p2_health = 10
mc.postToChat('THE GAME HAS BEGUN')
mc.postToChat(p1_name + ' vs. ' + p2_name)
mc.postToChat('USE A BOW TO SHOOT YOUR OPPONENT')
mc.postToChat('EACH PLAYER HAS ' + str(p1_health) + ' HEALTH')



while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        print("You hit block ({},{},{})".format(hit.pos.x, hit.pos.y, hit.pos.z))
    time.sleep(0.1)


    for proj in mc.events.pollProjectileHits():
        print(proj)
        if proj.originName == p1_name and proj.targetName == p2_name:
            if p2_health > 0:
                p2_health -= 1
                mc.postToChat(p1_name + ' has hit ' + p2_name)
                mc.postToChat(p2_name + ' has ' + str(p2_health) + ' health left')
            else:
                mc.postToChat(p1_name + ' has hit ' + p2_name + ' and killed him!')
                mc.entity.setTilePos(p2_id, 100, -200, 100)

        if proj.originName == p2_name and proj.targetName == p1_name:
            if p1_health > 0:
                p1_health -= 1
                mc.postToChat(p2_name + ' has hit ' + p1_name)
                mc.postToChat(p1_name + ' has ' + str(p1_health) + ' health left')
            else:
                mc.postToChat(p1_name + ' has hit ' + p2_name + ' and killed him!')
                mc.entity.setTilePos(p1_id, 100, -200, 100)
