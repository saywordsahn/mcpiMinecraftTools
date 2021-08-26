from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create("mc2.tokyocodingclub.com")

player = mc.getPlayerEntityId("TCC_03")

pos = mc.entity.getTilePos(player)


def copy(l, w, h):
    pos = mc.entity.getTilePos(player)

    blockInfo = []

    for i in range(l):
        x = []
        for j in range(h):
            y = []
            for k in range(w):
                block = mc.getBlock(pos.x + i, pos.y + j, pos.z + k)
                y.append(block)
            x.append(y)
        blockInfo.append(x)

    return blockInfo

def paste(blockInfo):
    pos = mc.entity.getTilePos(player)

    for i in range(len(blockInfo)):
        for j in range(len(blockInfo[i])):
            for k in range(len(blockInfo[i][j])):
                mc.setBlock(pos.x + i, pos.y + j, pos.z + k, blockInfo[i][j][k])


blockInfo = []
user_input = '-1'

while user_input != '3':
    print('1. Copy')
    print('2. Paste')
    print('3. Exit')
    print()
    user_input = input('Enter your selection (1-3): ')

    if user_input == '1':
        length = int(input('Enter length: '))
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))
        blockInfo = copy(length, width, height)
    if user_input == '2':
        print('pasting')
        paste(blockInfo)


