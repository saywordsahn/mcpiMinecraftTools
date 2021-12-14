import random

from mcpi.minecraft import Minecraft
import time
import random as rand
mc = Minecraft.create("mc.tokyocodingclub.com")


class Block:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p1_name = 'TCC_10'
p2_name = 'HYPER_TOHMA'

p1_id = mc.getPlayerEntityId(p1_name)
p2_id = mc.getPlayerEntityId(p2_name)

# create array of random blocks

p1_pos = mc.entity.getTilePos(p1_id)
max_distance = 30
num_blocks = 30
blockType = 7

blocks = {}
num_blocks_generated = 0
while num_blocks_generated < num_blocks:

    randx = p1_pos.x + random.randint(0, max_distance)
    randy = p1_pos.y + random.randint(0, max_distance)
    randz = p1_pos.z + random.randint(0, max_distance)

    if (randx, randy, randz) not in blocks.values():
        blocks[(randx, randy, randz)] = True
        num_blocks_generated += 1


# build the blocks
for key in blocks:
    print(key, blocks[key])
    mc.setBlock(key[0], key[1], key[2], blockType)

while num_blocks_generated > 0:

    for hit in mc.events.pollProjectileHits():
        print(hit)


