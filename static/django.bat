@echo off
@echo "Escribe el nombre del proyecto django: "
set /p proj_name=
set building="Building Django project %proj_name%"
@echo %building%
python c:/Python27/Scripts/Django-admin.py startproject %proj_name%
pause