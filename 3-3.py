from mcpi.minecraft import Minecraft
PY=Minecraft.create()
import random,time
while True:
    x,y,z=PY.player.getPos()
    a=random.uniform(-20,20)
    b=random.uniform(-20,20)
    y=y+3
    PY.spawnEntity(x+a,y,z+b,93)
    time.sleep(0.1)