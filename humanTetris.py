from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create("mc2.tokyocodingclub.com")

PP = mc.player.getPos()

LC = 3
max_level = 0
lose = False

sleeptime = 0.5

mc.setBlocks(PP.x - 4, PP.y - 1, PP.z - 1, PP.x + 3, PP.y + 8, PP.z + 51, 89)
mc.setBlocks(PP.x - 3, PP.y, PP.z, PP.x + 2, PP.y + 7, PP.z + 50, 0)

mc.setBlocks(PP.x - 3, PP.y, PP.z, PP.x + 2, PP.y + 7, PP.z, 213)
mc.setBlocks(PP.x, PP.y + 1, PP.z, PP.x, PP.y + 2, PP.z, 0)

for level in range(20):
    max_level = level + 1
    mc.postToChat("Level: " + str(max_level))
    mc.postToChat("You have " + str(LC) + " lives")

    number_of_lava = 0

    if level % 2 == 0:
        sleeptime = sleeptime / 2
    else:
        number_of_lava = level * 5

    rx = random.randint(-2, 1)
    ry = random.randint(1, 4)

    for blab in range(number_of_lava):
        lrx = random.randint(-3, 2)
        lry = random.randint(0, 7)
        lrz = random.randint(0, 50)
        mc.setBlock(PP.x + lrx, PP.y + lry, PP.z + lrz, 8)

    for i in range(50):
        time.sleep(sleeptime)
        mc.setBlocks(PP.x - 3, PP.y, PP.z + i + 1, PP.x + 2, PP.y + 7, PP.z + i + 1, 213)
        mc.setBlocks(PP.x + rx, PP.y + ry, PP.z + i + 1, PP.x + rx, PP.y + 2 + ry, PP.z + i + 1, 0)
        mc.setBlocks(PP.x - 3, PP.y, PP.z + i, PP.x + 2, PP.y + 7, PP.z + i, 0)
        newPP = mc.player.getPos()
        if mc.getBlock(newPP.x, newPP.y, newPP.z) == 213:
            mc.postToChat("You got hit")
            LC = LC - 1
            mc.postToChat("You have " + str(LC) + " lives")
            if LC == 0:
                lose = True
                break

    if lose:
        break

    for blab in range(number_of_lava):
        lrx = random.randint(-3, 2)
        lry = random.randint(0, 7)
        lrz = random.randint(0, 50)
        mc.setBlock(PP.x + lrx, PP.y + lry, PP.z + lrz, 8)

    rx = random.randint(-2, 1)
    ry = random.randint(1, 4)
    for i in range(50, 0, -1):
        time.sleep(sleeptime)
        mc.setBlocks(PP.x - 3, PP.y, PP.z + i, PP.x + 2, PP.y + 7, PP.z + i, 0)
        mc.setBlocks(PP.x - 3, PP.y, PP.z + i - 1, PP.x + 2, PP.y + 7, PP.z + i - 1, 213)
        mc.setBlocks(PP.x + rx, PP.y + ry, PP.z + i - 1, PP.x + rx, PP.y + 2 + ry, PP.z + i - 1, 0)
        newPP = mc.player.getPos()
        if mc.getBlock(newPP.x, newPP.y, newPP.z) == 213:
            mc.postToChat("You got hit")
            LC = LC - 1
            mc.postToChat("You have " + str(LC) + " lives")
            if LC == 0:
                lose = True
                break

    if lose:
        break

mc.postToChat("Game Over")
mc.postToChat("You have lived until level " + str(max_level))
mc.setBlocks(PP.x - 4, PP.y - 1, PP.z - 1, PP.x + 3, PP.y + 8, PP.z + 51, 0)
