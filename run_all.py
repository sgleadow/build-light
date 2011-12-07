#!/usr/bin/env python

import os
from buildlight import *

if __name__ == '__main__':
    # runs all jobs if jobs is not specified
    jenkins_host = 'localhost'
    try:
        jenkins_host = os.environ['BUILD_LIGHT_HOST']
    except KeyError:
        pass
        
    build_light = HudsonBuildLight(host=jenkins_host, port=8080, jobs=None)
    build_light.loop()
