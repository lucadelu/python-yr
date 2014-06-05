#!/usr/bin/env python3

from yr.libyr import Yr
from yr.verda import Verda

world = Verda()

for location in world.search('Prague'):
    now = Yr(location).now()
    print(location, now['temperature']['@value'], now['temperature']['@unit'])
