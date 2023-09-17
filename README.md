# rtCampAssignment - Devops Automation
Devops Taks Details
Create a command-line script, preferably in Bash, PHP, Node, or Python to perform the following tasks:

Check if docker and docker-compose is installed on the system. If not present, install the missing packages.
The script should be able to create a WordPress site using the latest WordPress Version. Please provide a way for the user to provide the site name as a command-line argument.
It must be a LEMP stack running inside containers (Docker) and a docker-compose file is a must.
Create a /etc/hosts entry for example.com pointing to localhost. Here we are assuming the user has provided example.com as the site name.
Prompt the user to open example.com in a browser if all goes well and the site is up and healthy.
Add another subcommand to enable/disable the site (stopping/starting the containers)
Add one more subcommand to delete the site (deleting containers and local files).
