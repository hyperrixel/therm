# therm

## What is this

This ` python ` script displays thermal zone temperatures in human readable format on Linux systems. Data is displayed in Celsius degrees. The conception of the script is based on Linux kernel's documentation from [here](https://www.kernel.org/doc/Documentation/thermal/sysfs-api.txt) and [here](https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/thermal/thermal.txt).

## Installation

Download the repository and run the script.

## Usage

This script doesn't require any parameters.

## Change behavior

If - for any reason - you system uses different directory and/or file names than the kernel's documentation, you can change some variables listed below to use Therm.

- ` THERMAL_BASEDIR ` Absolute path of the directory of thermal zone files.

- ` THERMAL_ZONE_PREFIX ` Prefix string of thermal zone files. Wildcards doesn't needed.

- ` THERMAL_ZONE_TEMP ` Suffix (ending) of temperature files.

- ` THERMAL_ZONE_TYPE ` Suffix (ending) of name files.
