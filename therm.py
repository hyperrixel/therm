#!/usr/bin/python3
"""
        _                 _
       (_)               | |
 _ __   _  __  __   ___  | |
| '__| | | \ \/ /  / _ \ | |
| |    | |  >  <  |  __/ | |
|_|    |_| /_/\_\  \___| |_|


THERM
=====

This script displays thermal zone temperatures in human readable format on linux
systems. Data is displayed in Celsius degrees.

The workflow of the code is based on the documentations:
https://www.kernel.org/doc/Documentation/thermal/sysfs-api.txt
https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/thermal/thermal.txt

Copyright rixel 2020
Distributed under the Boost Software License, Version 1.0.
See accompanying file LICENSE or a copy at https://www.boost.org/LICENSE_1_0.txt
"""



from os import listdir
from os.path import isdir, isfile, join
from sys import platform, exit



# Modify these lines in case if your OS uses different names or locations for
# thermal zones.
THERMAL_BASEDIR = '/sys/devices/virtual/thermal'
THERMAL_ZONE_PREFIX = 'thermal_zone'
THERMAL_ZONE_TEMP = 'temp'
THERMAL_ZONE_TYPE = 'type'



def main():

    global THERMAL_BASEDIR
    global THERMAL_ZONE_PREFIX
    global THERMAL_ZONE_TEMP
    global THERMAL_ZONE_TYPE

    if not (platform == 'linux' or platform == 'linux2'):
        print('This script requires Linux operating system!')
        exit(2)
    if not isdir(THERMAL_BASEDIR):
        print('Couldn\'t find base directory of thermal zones!')
        exit(3)
    thermal_zones = []
    for dir in listdir(THERMAL_BASEDIR):
        if isdir(join(THERMAL_BASEDIR, dir)):
            if dir.find(THERMAL_ZONE_PREFIX) != -1:
                thermal_zones.append(dir)
    thermdata = {}
    for zone in thermal_zones:
        zonepath = join(THERMAL_BASEDIR, zone)
        zone_type = join(zonepath, THERMAL_ZONE_TYPE)
        if not isfile(zone_type):
            continue
        zone_temp = join(zonepath, THERMAL_ZONE_TEMP)
        if not isfile(zone_temp):
            continue
        with open(zone_type, 'r') as instream:
            ztype = instream.read().strip()
        with open(zone_temp, 'r') as instream:
            zterm = instream.read().strip()
        if not zterm.isnumeric():
            continue
        thermdata[ztype] = float(zterm) / 1000.0
    if len(thermdata) > 0:
        print('Available thermal values on your system:')
        print('========================================')
        print('Zone identifier | Temperature in celsius')
        for name, value in thermdata.items():
            print('{:>15} : {:6.2f} oC'.format(name, value))



if __name__ == '__main__':
    main()
else:
    print('This is a script, not a module!')
    exit(1)
