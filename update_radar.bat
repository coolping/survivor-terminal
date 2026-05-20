@echo off
chcp 65001 >nul
title SURVIVOR TERMINAL // RADAR UPDATER
color 0A
cls

:: 執行 Python 掃描腳本
python scan_logs.py

echo.
pause