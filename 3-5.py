from mcpi.minecraft import Minecraft
PY=Minecraft.create()
x,y,z=PY.player.getTilePos()
for i in range(0,20):
    PY.setBlock(x,y,z+i,95)

