import os
import subprocess


def start_wordpress(site_name):
    # currdir = os.getcwd()
    # parentdir = os.path.abspath(os.path.join(currdir, os.pardir))
    # os.chdir(site_name)
    subprocess.run(['docker-compose', '-f', f'{site_name}/docker-compose.yml', 'up', '-d', '--build'])
    print(f"Please open {site_name} in your browser to access the site.")
    # os.chdir(parentdir)


def stop_wordpress(site_name):
    # currdir = os.getcwd()
    # parentdir = os.path.abspath(os.path.join(currdir, os.pardir))
    # os.chdir(site_name)
    subprocess.run(['docker-compose', '-f', f'{site_name}/docker-compose.yml', 'down'])
    # os.chdir(parentdir)

