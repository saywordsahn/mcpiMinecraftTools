from mcpi.minecraft import Minecraft
import time
from mcpi.minecraft import ProjectileEvent

mc = Minecraft.create("mc2.tokyocodingclub.com")

p1_name = 'TCC_10'

p1_id = mc.getPlayerEntityId(p1_name)



while True:

    for proj in mc.events.pollProjectileHits():
        print(proj)
        x = proj.pos.x
        y = proj.pos.y
        z = proj.pos.z
        mc.spawnEntity(x, y, z, 20)
        mc.setBlock(x, y, z, 46)




