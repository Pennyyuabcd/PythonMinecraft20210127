from mcpi.minecraft import Minecraft
PY=Minecraft.create()
while True:
    hits=PY.events.pollProjetileHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        PY.createExplosion(x,y,z,power=150)

