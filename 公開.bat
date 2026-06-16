@echo off
REM Double-click this file to publish the latest changes to the web.
REM It commits, pushes to GitHub, and Netlify auto-deploys.
powershell -ExecutionPolicy Bypass -File "%~dp0publish.ps1"
echo.
pause
