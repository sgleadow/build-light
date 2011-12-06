#!/usr/bin/env python

from buildlight import *

if __name__ == '__main__':
    # runs all jobs if jobs is not specified
    build_light = HudsonBuildLight(host='localhost', port=8081, jobs=None)
    build_light.loop()
