from cx_Freeze import setup, Executable
import sys

base = 'Win32GUI' if sys.platform == 'win32' else None

# This function builds the frozen executable
setup(
    name = "DailyWiki",
    version = "0.1",
    description = "A simple app to read a random Wikipedia article every day!",
    executables = [Executable("main.py", base=base)],
)