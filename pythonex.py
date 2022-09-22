import pkg_resources
import subprocess
import sys



required = {'colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

print(missing)

if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

from colorama import Fore

print(f'{Fore.GREEN} Hi with green! {Fore.RESET}')