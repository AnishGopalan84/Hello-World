#!/usr/bin/env python
import subprocess
uname = "uname"
uname_arg = "-a"
print("Gathering Sys Info using %s command:\n")
subprocess.call([uname, uname_arg])
diskspace = "df"
diskspace_arg = "-h"
print("Gathering Hdd Info using %s command:\n")
subprocess.call([diskspace, diskspace_arg])

subprocess.call(["ls"])
