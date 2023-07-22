#!/usr/bin/env python3

import platform
import subprocess
import sys


def install_docker_linux():
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "install", "-y", "docker.io"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)
    subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)


def install_docker_macos():
    subprocess.run(["brew", "install", "docker"], check=True)
    subprocess.run(["brew", "services", "start", "docker"], check=True)


def install_docker_windows():
    print("Please download and install Docker Desktop for Windows from the official website.")
    sys.exit(1)


def platform_check():
    if platform.system() == "Linux":
        install_docker_linux()
    elif platform.system() == "Darwin":  # macOS
        install_docker_macos()
    elif platform.system() == "Windows":
        install_docker_windows()
    else:
        print("Unsupported operating system.")
        sys.exit(1)


