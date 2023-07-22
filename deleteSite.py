import subprocess
import os


def stop_and_remove_containers(site_name):
    subprocess.run(['docker-compose', '-f', f'{site_name}/docker-compose.yml', 'down'])


def clean_up_volumes():
    subprocess.run(['docker', 'volume', 'prune', '-f'])


def clean_up_networks():
    subprocess.run(['docker', 'network', 'prune', '-f'])


def replace_line_in_file(target_line):
    with open('/etc/hosts', 'r') as infile, open('/etc/hosts', 'w') as outfile:
        for line in infile:
            if line.strip() == target_line.strip():
                outfile.write('\n')
            else:
                outfile.write(line)


def cleanSite(site_name, target_line):
    # currdir = os.getcwd()
    # parentdir = os.path.abspath(os.path.join(currdir, os.pardir))
    # os.chdir(site_name)
    stop_and_remove_containers(site_name)
    clean_up_volumes()
    clean_up_networks()
    replace_line_in_file(target_line)
    # os.chdir(parentdir)
    subprocess.run(['rm', '-rf', site_name])
