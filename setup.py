from cx_Freeze import setup, Executable


#base = None

executables = [Executable("ui.py")]

##packages ["idna"]
##options = {
##    'build_exe': {
##        'packages':packages,
##        },
##
##    }

setup(
    name = "spendingTracker",
    #options = options,
    version = "1.0",
    description = "A simple spending tracker",
    executables = executables
)
