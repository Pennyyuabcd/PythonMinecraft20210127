from mcpi.minecraft import Minecraft
import random,time
PY=Minecraft.create()
while True:
    x,y,z=PY.player.getTilePos()
    color=random.randrange(0,9)
    PY.setBlock(x,y,z,38,color)
    time.sleep(1)

