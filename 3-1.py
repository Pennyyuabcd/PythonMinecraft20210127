from mcpi.minecraft import Minecraft
PY=Minecraft.create()
while True:
    hits=PY.events.pollBlockHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        block=PY.getBlock(x,y,z)
        PY.postToChat("你打到了"+str(block))
        
        


