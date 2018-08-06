from cx_Freeze import setup, Executable

target = Executable(
    script="your_program.py",
    base="Win32GUI",
    compress=False,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon="icon.ico"
    )

setup(
    name="name",
    version="1.0",
    description="the description",
    author="the author",
    options={"build_exe": options},
    executables=[target]
    )
