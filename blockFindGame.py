from mcpi.minecraft import Minecraft
import random as rand
import math
import time

blockCode = 3

mc = Minecraft.create('mc2.tokyocodingclub.com')

ben = mc.getPlayerEntityId('TCC_10')

pos = mc.entity.getTilePos(ben)
x = rand.randint(pos.x + 50, pos.x + 100)
y = rand.randint(pos.y + 50, pos.y + 100)
z = rand.randint(pos.z + 50, pos.z + 100)

mc.setBlock(x, y, z, blockCode)
mc.postToChat('THE BLOCK HAS BEEN PLACED')
mc.postToChat('YOU MAY BEGIN!')

while True:
    pos = mc.entity.getTilePos(ben)

    diffX = math.pow(pos.x - x, 2)
    diffY = math.pow(pos.y - y, 2)
    diffZ = math.pow(pos.z - z, 2)
    dist = math.sqrt(diffX + diffY + diffZ)

    if dist < 2.0:
        # set new block
        mc.postToChat('GREAT JOB, A NEW BLOCK HAS SPAWNED!')
        x = rand.randint(pos.x + 50, pos.x + 100)
        y = rand.randint(pos.y + 50, pos.y + 100)
        z = rand.randint(pos.z + 50, pos.z + 100)
        mc.setBlock(x, y, z, blockCode)


    mc.postToChat(dist)
    time.sleep(1)