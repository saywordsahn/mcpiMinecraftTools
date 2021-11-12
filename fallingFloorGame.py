from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random


mc = Minecraft.create("mc2.tokyocodingclub.com")
me = mc.getPlayerEntityId("TCC_10")
x, y, z = mc.entity.getTilePos(me)

block.SLIME = 165
block.SEA_LANTERN = 169

def build_walls(minecraft_var, x, y, z, size, levels, levels_height):
    minecraft_var.setBlocks(x - size - 1, 0, z - size - 1, x + size + 1, levels * levels_height + 1, z + size + 1,
                            block.SEA_LANTERN)
    minecraft_var.setBlocks(x - size, 0, z - size, x + size, levels * levels_height, z + size, block.AIR)

def build_levels(minecraft_var, x, y, z, size, levels, levels_height):
    for i in range(levels):
        minecraft_var.setBlocks(x - size, i * levels_height, z - size, x + size, i * levels_height, z + size,
                                block.SLIME)

class ActiveBlock:

    def __init__(self, x, y, z, start_time):
        self.x = x
        self.y = y
        self.z = z
        self.start_time = start_time

levels = 5
size = 5
height = 10
active_blocks = []
block_alive_time = .7

floor_block = block.IRON_BLOCK

build_walls(mc, x, y, z, size, levels, height)
build_levels(mc, x, y, z, size, levels, height)

start = -1
now = -1
printed_value = 0
hardmode = False

my_level = 0

lv1 = 50
lv2 = 40
lv3 = 30
lv4 = 20
lv5 = 10
DEATH = 0
mc.postToChat("someone had started the game!")

while True:
    # get blocks under you
    x, y, z = mc.entity.getTilePos(me)

    # if slime block then get rid of it
    # for i in range(-1, 2):
    #     for j in range(-1, 2):
    #         kaboom = mc.getBlock(x + i, y - 1, z + j)
    #         if kaboom == 165:
    #             mc.setBlock(x + i, y - 1, z + j, 0)

    under_block = mc.getBlock(x, y - 1, z)

    if under_block == 165:
        active_block = ActiveBlock(x, y - 1, z, time.time())
        active_blocks.append(active_block)

    for block in active_blocks:
        if time.time() - block.start_time > block_alive_time:
            mc.setBlock(block.x, block.y, block.z, 0)

    if y < lv1 and y > lv2 and my_level != 1:
        my_level = 1
        mc.postToChat("someone dropped to level 1!")
        start = time.time()
        mc.postToChat(start)

    if y < lv2 and y > lv3 and my_level != 2:
        my_level = 2
        mc.postToChat("someone dropped to level 2.")

    if y < lv3 and y > lv4 and my_level != 3:
        my_level = 3
        mc.postToChat("someone dropped to level 3...")

    if y < lv4 and y > lv5 and my_level != 4:
        my_level = 4
        mc.postToChat("someone dropped to level 4:(")

    if y < lv5 and y > DEATH and my_level != 5:
        my_level = 5
        mc.postToChat("someone dropped to level 5... :'(")

    if y < DEATH and my_level != 1000:
        my_level = 1000
        mc.postToChat("someone just died... XD")

    if start > 0:
        now = time.time()
        elapsed_time = int(now - start)
        if elapsed_time % 5 == 0 and elapsed_time != printed_value:
            mc.postToChat(elapsed_time)
            printed_value = elapsed_time

            if elapsed_time > 50:
                hardmode = True
                if hardmode == True:
                    mc.setBlocks(x, 0, z, x + 5, 60, z + 5, 42)
