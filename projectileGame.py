from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

p1_name = 'TCC_10'
p2_name = 'TCC_09'

p1_id = mc.getPlayerEntityId(p1_name)
p2_id = mc.getPlayerEntityId(p2_name)

while True:

    hits = mc.events.pollBlockHits()
    for hit in hits:
        print("You hit block ({},{},{})".format(hit.pos.x, hit.pos.y, hit.pos.z))
    time.sleep(0.1)


    for proj in mc.events.pollProjectileHits():
        print(proj)
        if proj.originName == p1_name and proj.targetName == p2_name:
            mc.postToChat(p1_name + ' has hit ' + p2_name + ' and killed him!')
            # teleport p2 to -1000 y level
            pass

        if proj.originName == p2_name and proj.targetName == p1_name:
            mc.postToChat(p2_name + ' has hit ' + p1_name + ' and killed him!')
            #teleport p1 to -1000 y level
            pass



