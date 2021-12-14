import random
from mcpi.minecraft import Minecraft
import time
import random as rand
mc = Minecraft.create("mc.tokyocodingclub.com")

player = 'TCC_10'
target = 'HYPER_TOHMA'

player_id = mc.getPlayerEntityId(player)
target_id = mc.getPlayerEntityId(target)


while True:
    # get largest distance away from x, y, z

    player_loc = mc.entity.getTilePos(player_id)
    target_loc = mc.entity.getTilePos(target_id)

    x_dist = target_loc.x - player_loc.x
    y_dist = target_loc.y - player_loc.y
    z_dist = target_loc.z - player_loc.z


    if (x_dist >= y_dist) and (x_dist >= z_dist):
        # largest diff is x dist
        if x_dist > 0:
            mc.postToChat('Go East')
        else:
            mc.postToChat('Go West')
        largest = x_dist
    elif (y_dist >= x_dist) and (y_dist >= z_dist):
        # largest diff is y dist
        if y_dist > 0:
            mc.postToChat('Go up')
        elif y_dist < 0:
            mc.postToChat('Go down')
    else:
        if z_dist > 0:
            mc.postToChat('Go South')
        else:
            mc.postToChat('Go North')

    time.sleep(1)
