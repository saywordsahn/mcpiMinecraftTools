from mcpi.minecraft import Minecraft
from mcpi import block
import time
from enum import Enum

mc = Minecraft.create("mc2.tokyocodingclub.com")


def spawn_iron_golem(x, y, z):
    mc.setBlock(x, y, z, block.IRON_BLOCK)
    mc.setBlock(x, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x + 1, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x - 1, y + 1, z, block.IRON_BLOCK)
    mc.setBlock(x, y + 2, z, block.PUMPKIN)


class HitAction(Enum):
    SecretGate = 1,
    Teleport = 2,


class Block:

    def __init__(self, x, y, z, type):
        self.x = x
        self.y = y
        self.z = z
        self.type = type

class TeleportBlock(Block):

    def __init__(self, x, y, z, tx, ty, tz):
        Block.__init__(self, x, y, z, HitAction.Teleport)
        self.tx = tx
        self.ty = ty
        self.tz = tz

    def teleport(self, playerId):
        mc.entity.setTilePos(playerId, self.tx, self.ty, self.tz)



p1_name = 'KamuiLinkPro'
p2_name = 'TCC_10'

p1_id = mc.getPlayerEntityId(p1_name)
p2_id = mc.getPlayerEntityId(p2_name)

permissions = {p1_id: True, p2_id: True}

# SET UP BLOCKS ###############
###############################
secretBlock = Block(-484, 17, -1006, HitAction.SecretGate)
tpBlock = TeleportBlock(-497, 11, -1016, -496, 20, -1016)
blocks = [secretBlock, tpBlock]

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
        print(event)
        # if permissions[event.entityId]:
        for b in blocks:
            if (event.pos.x == b.x
                    and event.pos.y == b.y
                    and event.pos.z == b.z):
                if b.type == HitAction.SecretGate:
                    filled = not filled
                    x, y, z = event.pos

                    if filled:
                        mc.setBlocks(x + 1, y, z + 1, x + size, y + size, z + size, block.WOOD_PLANKS)
                        mc.postToChat('the path has been closed')
                    else:
                        mc.setBlocks(x + 1, y, z + 1, x + size, y + size, z + size, block.AIR)
                        mc.postToChat('the path has been cleared')
                elif b.type == HitAction.Teleport:
                    b.teleport(event.entityId)
                    mc.postToChat('Someone was thrown into the air!')

    time.sleep(.4)
