import subprocess
import platform


def clear():
    if platform.system() == "Windows":
        subprocess.run('cls', shell=True)  # nosec B602, B607
    else:
        subprocess.run('clear', shell=True)  # nosec B602, B607
