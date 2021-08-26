from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create("mc2.tokyocodingclub.com")

def spawn_iron_golem(x, y, z):
    mc.setBlock(x, y, z, block.IRON_BLOCK)
    mc.setBlock(x, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x + 1, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x - 1, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x, y + 2, z, block.PUMPKIN)

p1_name = 'KamuiLinkPro'
p2_name = 'TCC_05'

p1_id = mc.getPlayerEntityId(p1_name)
p2_id = mc.getPlayerEntityId(p2_name)

permissions = {p1_id: True, p2_id: True}

print(p1_id)
print(p2_id)
filled = True
x, y, z = 0, 0, 0
size = 3

while True:
    hits = mc.events.pollBlockHits()
    # for event in hits:
    #     print(event.pos)
    #     spawn_iron_golem(event.pos.x + 1, event.pos.y, event.pos.z + 1)
    #     mc.postToChat('the switch has been hit')
    for event in hits:

        # if permissions[event.entityId]:
        filled = not filled
        x, y ,z = event.pos

        if filled:
            mc.setBlocks(x + 1, y, z + 1, x + size, y + size, z + size, block.WOOD_PLANKS)
            mc.postToChat('the path has been closed')
        else:
            mc.setBlocks(x + 1, y, z + 1, x + size, y + size, z + size, block.AIR)
            mc.postToChat('the path has been cleared')

    if filled:
        mc.setBlocks(x + 1, y, z + 1, x + size, y + size, z + size, block.WOOD_PLANKS)
    time.sleep(.4)


