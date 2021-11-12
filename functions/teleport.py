from mcpi.minecraft import Minecraft

def teleport(server, sourceName, targetName):
    mc = Minecraft.create(server)

    sourceId = mc.getPlayerEntityId(sourceName)
    targetId = mc.getPlayerEntityId(targetName)

    tpos = mc.entity.getTilePos(targetId)

    mc.entity.setTilePos(sourceId, tpos.x, tpos.y, tpos.z)
