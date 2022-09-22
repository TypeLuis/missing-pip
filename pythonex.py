import pkg_resources
import subprocess
import sys



required = {'colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

print(missing)

