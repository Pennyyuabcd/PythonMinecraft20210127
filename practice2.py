from mcpi.minecraft import Minecraft
PY=Minecraft.create()
while True:
    hits=PY.events.pollProjectileHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        PY.player.setTilePos(x,y,z)
        PY.spawnEntity(x,y,z,99)
        
