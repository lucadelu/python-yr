#!/usr/bin/env python3

from yr.libyr import Yr
from yr.verda import Verda

world = Verda()

for location_name in world.search('Prague'):
    now = Yr(location_name=location_name).now()
    print(location_name, now['temperature']['@value'], now['temperature']['@unit'])
