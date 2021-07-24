from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)

length = 30
width = 30
height = 20
useGlass = True
light_source = 169

# # left wall
# for i in range(length):
#     for j in range(height):
#             if useGlass:
#                 if i % 5 == 0 and j % 5 == 0 and j != 0 and j != height:
#                     mc.setBlock(pos.x + i, pos.y + j, pos.z, 168)
#                     mc.setBlock(pos.x + i, pos.y + j, pos.z  - 1, light_source)
#             else:
#                 if i % 5 == 0 and j % 5 == 0:
#                     mc.setBlock(pos.x + i, pos.y + j, pos.z, light_source)
#
# # right wall
# for i in range(length):
#     for j in range(height):
#             if useGlass:
#                 if i % 5 == 0 and j % 5 == 0 and j != 0 and j != height:
#                     mc.setBlock(pos.x + i, pos.y + j, pos.z + 1, 169)
#                     mc.setBlock(pos.x + i, pos.y + j, pos.z, block.GLASS)
#             else:
#                 if i % 5 == 0 and j % 5 == 0:
#                     mc.setBlock(pos.x + i, pos.y + j, pos.z, light_source)

#
# # far wall
# for i in range(width):
#     for j in range(height):
#             if useGlass:
#                 if i % 5 == 0 and j % 5 == 0 and j != 0 and j != height:
#                     mc.setBlock(pos.x + 1, pos.y + j, pos.z + i, 169)
#                     mc.setBlock(pos.x, pos.y + j, pos.z + i, block.GLASS)
#             else:
#                 if i % 5 == 0 and j % 5 == 0:
#                     mc.setBlock(pos.x + i, pos.y + j, pos.z, light_source)



# behind wall
for i in range(width):
    for j in range(height):
            if useGlass:
                if i % 5 == 0 and j % 5 == 0 and j != 0 and j != height:
                    mc.setBlock(pos.x - 2, pos.y + j, pos.z + i, 169)
                    mc.setBlock(pos.x - 1, pos.y + j, pos.z + i, block.GLASS)
            else:
                if i % 5 == 0 and j % 5 == 0:
                    mc.setBlock(pos.x - 1, pos.y + j, pos.z, light_source)