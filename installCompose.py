import os
import platform
import subprocess
import sys


def install_docker_compose():
    system = platform.system().lower()

    if system == 'linux':
        # Install Docker Compose on Linux
        subprocess.run(['sudo', 'curl', '-L',
                        'https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)',
                        '-o', '/usr/local/bin/docker-compose'])
        subprocess.run(['sudo', 'chmod', '+x', '/usr/local/bin/docker-compose'])

    elif system == 'darwin':
        # Install Docker Compose on macOS
        subprocess.run(['curl', '-L',
                        'https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)',
                        '-o', '/usr/local/bin/docker-compose'])
        subprocess.run(['chmod', '+x', '/usr/local/bin/docker-compose'])

    elif system == 'windows':
        # Install Docker Compose on Windows
        subprocess.run(['curl', '-L',
                        'https://github.com/docker/compose/releases/latest/download/docker-compose-Windows-x86_64.exe',
                        '-o', 'docker-compose.exe'])
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + os.getcwd()

    else:
        print("Unsupported operating system:", system)
        sys.exit(1)

    print("Docker Compose has been installed successfully!")


