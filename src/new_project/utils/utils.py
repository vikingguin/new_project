import os
import platform

def clear_console():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    os.system(command)