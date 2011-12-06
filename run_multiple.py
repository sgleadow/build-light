#!/usr/bin/env python

from buildlight import *

if __name__ == '__main__':
    job_names = [ 'Meryl', 'Norris', 'Marvin', 'Smoke%20Test', 'Distribution', 'iOS5%20Smoke%20Test' ]
    build_light = HudsonBuildLight(host='localhost', port=8081, jobs=job_names)
    build_light.loop()
