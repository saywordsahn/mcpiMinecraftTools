from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_10")

pos = mc.entity.getTilePos(player)

length = 100
width = 10
useGlass = True
floor = True
ceiling = False
light_source = 169

for i in range(length):
    for j in range(width):
        if floor:
            if useGlass:
                if i % 5 == 0 and j % 5 == 0:
                    mc.setBlock(pos.x + i, pos.y - 1, pos.z + j, block.GLASS)
                    mc.setBlock(pos.x + i, pos.y - 2, pos.z + j, light_source)
            else:
                if i % 5 == 0 and j % 5 == 0:
                    mc.setBlock(pos.x + i, pos.y - 1, pos.z + j, light_source)

        if ceiling:
            if useGlass:
                if i % 5 == 0 and j % 5 == 0:
                    mc.setBlock(pos.x + i, pos.y + 2, pos.z + j, block.GLASS)
                    mc.setBlock(pos.x + i, pos.y + 3, pos.z + j, light_source)
            else:
                if i % 5 == 0 and j % 5 == 0:
                    mc.setBlock(pos.x + i, pos.y + 2, pos.z + j, light_source)