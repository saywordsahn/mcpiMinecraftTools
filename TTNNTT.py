from mcpi.minecraft import Minecraft

mc = Minecraft.create('mc.tokyocodingclub.com')
EID = mc.getPlayerEntityId('TCC_09')
XYZ = mc.entity.getTilePos(EID)
X = XYZ.x
Y = XYZ.y
Z = XYZ.z
##56ore diDIRECTI
DIRECTION = mc.entity.getDirection(EID)
print(DIRECTION)


def TNT_CANNNOOON(X, Y, Z, DIRECTION=DIRECTION):
    X_D = DIRECTION.x
    Z_D = DIRECTION.z
    if abs(X_D) > abs(Z_D):
        if X_D > 0:
            direction = "east"
        elif X_D < 0:
            direction = "west"
    else:
        if Z_D > 0:
            direction = "south"
        elif Z_D < 0:
            direction = "north"

    print(direction)
    # facing east
    if direction == 'east':
        mc.setBlocks(X - 1, Y - 1, Z - 2, X + 9, Y - 1, Z + 2, 56)
        mc.setBlocks(X + 2, Y, Z - 1, X + 2, Y, Z + 1, 56)
        mc.setBlock(X + 1, Y, Z + 1, 76, 2)
        mc.setBlock(X + 1, Y, Z - 1, 76, 2)
        mc.setBlock(X + 3, Y, Z - 1, 76, 1)
        mc.setBlock(X + 3, Y, Z + 1, 76, 1)
        mc.setBlocks(X + 2, Y + 1, Z + 1, X + 2, Y + 1, Z - 1, 55)
        mc.setBlock(X + 1, Y, Z, 55)
        mc.setBlock(X + 3, Y, Z, 55)
        mc.setBlocks(X + 7, Y, Z - 1, X + 7, Y, Z + 1, 44, 6)
        mc.setBlocks(X + 5, Y, Z - 1, X + 5, Y, Z + 1, 23, 5)
        mc.setBlock(X + 6, Y, Z - 2, 56)
        mc.setBlock(X + 6, Y, Z + 2, 56)
        mc.setBlocks(X + 6, Y, Z - 1, X + 6, Y, Z + 1, 8)
        mc.setBlocks(X + 6, Y + 1, Z - 1, X + 6, Y + 1, Z + 1, 23, 5)
        mc.setBlocks(X + 5, Y + 1, Z + 1, X + 5, Y + 1, Z - 1, 55)
        mc.setBlocks(X + 7, Y + 2, Z - 1, X + 7, Y + 2, Z + 1, 44, 6)
    if direction == 'west':

        mc.setBlocks(X + 1, Y - 1, Z - 2, X - 9, Y - 1, Z + 2, 56)
        mc.setBlocks(X - 2, Y, Z - 1, X - 2, Y, Z + 1, 56)
        mc.setBlock(X - 1, Y, Z + 1, 76, 1)
        mc.setBlock(X - 1, Y, Z - 1, 76, 1)
        mc.setBlock(X - 3, Y, Z - 1, 76, 2)
        mc.setBlock(X - 3, Y, Z + 1, 76, 2)
        mc.setBlocks(X - 2, Y + 1, Z + 1, X - 2, Y + 1, Z - 1, 55)
        mc.setBlock(X - 1, Y, Z, 55)
        mc.setBlock(X - 3, Y, Z, 55)
        mc.setBlocks(X - 7, Y, Z - 1, X - 7, Y, Z + 1, 44, 6)
        mc.setBlocks(X - 5, Y, Z - 1, X - 5, Y, Z + 1, 23, 4)
        mc.setBlock(X - 6, Y, Z - 2, 56)
        mc.setBlock(X - 6, Y, Z + 2, 56)
        mc.setBlocks(X - 6, Y, Z - 1, X - 6, Y, Z + 1, 8)
        mc.setBlocks(X - 6, Y + 1, Z - 1, X - 6, Y + 1, Z + 1, 23, 4)
        mc.setBlocks(X - 5, Y + 1, Z + 1, X - 5, Y + 1, Z - 1, 55)
        mc.setBlocks(X - 7, Y + 2, Z - 1, X - 7, Y + 2, Z + 1, 44, 6)
    if direction == 'north':
        mc.setBlocks(X - 2, Y - 1, Z + 1, X + 2, Y - 1, Z - 9, 56)
        mc.setBlocks(X - 1, Y, Z - 2, X + 1, Y, Z - 2, 56)
        mc.setBlock(X + 1, Y, Z - 1, 76, 3)
        mc.setBlock(X - 1, Y, Z - 1, 76, 3)
        mc.setBlock(X - 1, Y, Z - 3, 76, 4)
        mc.setBlock(X + 1, Y, Z - 3, 76, 4)
        mc.setBlocks(X + 1, Y + 1, Z - 2, X - 1, Y + 1, Z - 2, 55)
        mc.setBlock(X, Y, Z - 1, 55)
        mc.setBlock(X, Y, Z - 3, 55)
        mc.setBlocks(X - 1, Y, Z - 7, X + 1, Y, Z - 7, 44, 6)
        mc.setBlocks(X - 1, Y, Z - 5, X + 1, Y, Z - 5, 23, 2)
        mc.setBlock(X - 2, Y, Z - 6, 56)
        mc.setBlock(X + 2, Y, Z - 6, 56)
        mc.setBlocks(X - 1, Y, Z - 6, X + 1, Y, Z - 6, 8)
        mc.setBlocks(X - 1, Y + 1, Z - 6, X + 1, Y + 1, Z - 6, 23, 2)
        mc.setBlocks(X + 1, Y + 1, Z - 5, X - 1, Y + 1, Z - 5, 55)
        mc.setBlocks(X - 1, Y + 2, Z - 7, X + 1, Y + 2, Z - 7, 44, 6)
    if direction == 'south':
        mc.setBlocks(X - 2, Y - 1, Z - 1, X + 2, Y - 1, Z + 9, 56)
        mc.setBlocks(X - 1, Y, Z + 2, X + 1, Y, Z + 2, 56)
        mc.setBlock(X + 1, Y, Z + 1, 76, 4)
        mc.setBlock(X - 1, Y, Z + 1, 76, 4)
        mc.setBlock(X - 1, Y, Z + 3, 76, 3)
        mc.setBlock(X + 1, Y, Z + 3, 76, 3)
        mc.setBlocks(X + 1, Y + 1, Z + 2, X - 1, Y + 1, Z + 2, 55)
        mc.setBlock(X, Y, Z + 1, 55)
        mc.setBlock(X, Y, Z + 3, 55)
        mc.setBlocks(X - 1, Y, Z + 7, X + 1, Y, Z + 7, 44, 6)
        mc.setBlocks(X - 1, Y, Z + 5, X + 1, Y, Z + 5, 23, 3)
        mc.setBlock(X - 2, Y, Z + 6, 56)
        mc.setBlock(X + 2, Y, Z + 6, 56)
        mc.setBlocks(X - 1, Y, Z + 6, X + 1, Y, Z + 6, 8)
        mc.setBlocks(X - 1, Y + 1, Z + 6, X + 1, Y + 1, Z + 6, 23, 3)
        mc.setBlocks(X + 1, Y + 1, Z + 5, X - 1, Y + 1, Z + 5, 55)
        mc.setBlocks(X - 1, Y + 2, Z + 7, X + 1, Y + 2, Z + 7, 44, 6)
##mc.setBlocks(X, Y, Z, X+8, Y+8, Z+8, 56)
##mc.setBlocks(X+1, Y+1, Z+1, X+7, Y+7, Z+7, 0)
TNT_CANNNOOON(X, Y, Z, DIRECTION)

##mc.entity.setTilePos(EID, 360, 2, -1)