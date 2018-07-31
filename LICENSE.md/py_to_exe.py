from cx_Freeze import setup, Executable
 
setup(
    name = "EXE_app" ,
    version = "0.1" ,
    description = "TOOL ABOUT VENDOR.XML" ,
    executables = [Executable("GM_TOOL.py")] ,
    )
