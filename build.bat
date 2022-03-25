@echo off
pyinstaller -F -i Resources\img\icon.ico --add-data="Resources/img/icon.ico;Resources/img" -n Calculator Main.py --hidden-import xmltodict
set dir=dist\Resources\xml
if not exist %dir% mkdir %dir%
xcopy Resources\xml %dir% /e /y
pause