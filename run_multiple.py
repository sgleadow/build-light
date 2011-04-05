#!/usr/bin/env python

from buildlight import *

if __name__ == '__main__':
    job_names = ['first-job-name-here', 'and-any-other-job-names']
    build_light = HudsonBuildLight(host='localhost', port=8080, jobs=job_names)
    build_light.loop()
