from cx_Freeze import setup, Executable

setup(
    name = "DailyWiki",
    version = "1.0",
    description = "Get a new article from Wikipedia everyday!",
    executables = [Executable("DailyWiki.py", icon="wikipedia_iconblack.ico", base = "Win32GUI")],
    )




