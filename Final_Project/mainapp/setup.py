import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'c:/Users/Omkar/AppData/Local/Programs/Python/Python35/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/Users/Omkar/AppData/Local/Programs/Python/Python35/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['c:/Users/Omkar/AppData/Local/Programs/Python/Python35/DLLs/tcl86t.dll', 'c:/Users/Omkar/AppData/Local/Programs/Python/Python35/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('gui.py', base=base)
]

setup(name='editor',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)