from time import sleep
from buildlight import *

light = HudsonBuildLight(None, None, None)

for x in range(30):
    light.set_usbled_color(sys.argv[1])
    sleep(1)
    light.usbled.off()
    sleep(1)
