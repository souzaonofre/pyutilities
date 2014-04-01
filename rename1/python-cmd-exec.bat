@ECHO off

set kivy_portable_root=C:\Users\OSouza\Apps\Kivy\

IF DEFINED kivy_paths_initialized (GOTO :runpython)

set GST_REGISTRY=%kivy_portable_root%gstreamer\registry.bin

set GST_PLUGIN_PATH=%kivy_portable_root%gstreamer\lib\gstreamer-0.10

set PATH=%kivy_portable_root%;%kivy_portable_root%Python;%kivy_portable_root%Python\Scripts;%kivy_portable_root%gstreamer\bin;%kivy_portable_root%MinGW\bin;%PATH%

set PYTHONPATH=%kivy_portable_root%kivy

set kivy_paths_initialized=1


:runpython

%comspec% /Q

:end




