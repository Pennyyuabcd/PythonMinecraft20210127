from mcpi.minecraft import Minecraft
PY=Minecraft.create()
x,y,z=PY.player.getPos()
number = 1
for i in range(8):
    for j in range(number):
        PY.spawnEntity(x,y,z,60)
    number=number*2
    PY.postToChat("這次生成了"+str(number)+"隻蠧魚")
    