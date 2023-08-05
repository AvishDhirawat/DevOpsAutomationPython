#!/usr/bin/env python3

import subprocess
import sys

import createWordPress
import deleteSite
import installDocker
import installCompose
import startStopSite


def check_dependencies():
    print("Checking Docker and Docker Compose...")
    try:
        subprocess.run(["docker", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        subprocess.run(["docker-compose", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       check=True)
        print("Docker and Docker Compose are installed.")
    except subprocess.CalledProcessError:
        print("Docker or Docker Compose is not installed. Please install them and try again.")
        sys.exit(1)


def install_docker():
    print("Installing Docker in your system......")
    installDocker.platform_check()
    sys.exit(1)


def install_docker_compose():
    print("Installing Docker Compose in your system......")
    installCompose.install_docker_compose()
    sys.exit(1)


def create_wordpress_site(site_name):
    print(f"Creating WordPress site: {site_name}")
    createWordPress.createSite(site_name)


def enable_disable_site(enable, site_name):
    action = "starting" if enable else "stopping"
    print(f"{action.capitalize()} the WordPress site...")
    if enable:
        startStopSite.start_wordpress(site_name)
    else:
        startStopSite.stop_wordpress(site_name)


def delete_site(site_name, targetline):
    print(f"Deleting WordPress site: {site_name}")
    deleteSite.cleanSite(site_name, targetline)
    print(f"Site Deleted : {site_name}")


def main():
    if len(sys.argv) < 2:
        print("Usage: rtcampMain.py <command> <site_name>")
        print("Commands: create, enable, disable, delete")
        sys.exit(1)

    command = sys.argv[1]

    if command == "create":
        if len(sys.argv) < 3:
            print("Usage: rtcampMain.py create <site_name>")
            sys.exit(1)
        site_name = sys.argv[2]
        check_dependencies()
        create_wordpress_site(site_name)

        with open("/etc/hosts", "a") as hosts_file:
            hosts_file.write(f"127.0.0.1\t{site_name}\n")

        print("Site setup completed successfully!")
        

    elif command == "enable":
        if len(sys.argv) < 3:
            print("Usage: rtcampMain.py enable <site_name>")
            sys.exit(1)
        site_name = sys.argv[2]
        enable_disable_site(True, site_name)

    elif command == "disable":
        if len(sys.argv) < 3:
            print("Usage: rtcampMain.py disable <site_name>")
            sys.exit(1)
        site_name = sys.argv[2]
        enable_disable_site(False, site_name)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: rtcampMain.py delete <site_name>")
            sys.exit(1)
        site_name = sys.argv[2]
        targetline = f"127.0.0.1\t{site_name}\n"
        delete_site(site_name, targetline)

    else:
        print("Invalid command.")
        print("Commands: create, enable, disable, delete")
        sys.exit(1)


if __name__ == "__main__":
    main()
