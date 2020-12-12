#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
set -e
OLDDIR=$(pwd)


# Shuffle and select first file
# phosphor -root -delay 16522 -scale 3 -program cat `find /usr/src/linux-source/ -name '*.c' -or -name '*.h' | shuf | head -n1`
# /usr/lib64/misc/xscreensaver/apple2 -text -fast -program 'bash'
# /usr/lib/xscreensaver/phosphor -delay 10000 -scale 6 -ticks 3 -program 'cat `find /usr/src/linux-source/ -name '*.c' -or -name '*.h' | shuf | head -n1`'
# phosphor -root -delay 60000 -scale 6 -ticks 3 -program 'cat `find /usr/src/linux-source/ -name '*.c' -or -name '*.h' | shuf | head -n1`'
# phosphor -root -delay 1000 -scale 3 -ticks 3 -program 'cat `find /usr/src/linux-source/ -name '*.c' -or -name '*.h' | shuf | head -n1`'

cat `find /usr/src/linux-source/ -name '*.c' -or -name '*.h' | shuf | head -n1`