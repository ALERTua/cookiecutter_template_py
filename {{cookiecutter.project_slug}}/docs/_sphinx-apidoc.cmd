
@echo off
call %~dp0constants.cmd

"%venv_scripts%\sphinx-apidoc.exe" -f -o="%~dp0source" "%~dp0../{{ cookiecutter.project_slug }}" "**/tryouts*"
