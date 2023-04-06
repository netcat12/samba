# SambaTool
SambaTool is a Python script that can be used to mount a Samba share on a Unix-like system using the CIFS protocol. It prompts the user for the necessary information (server name, share name, username, password, mount point, etc.) and executes the mount command using the subprocess module. It also provides an option to unmount the share after use.


# Requirement 
SambaTool requires Python 3 and the following packages:

os
subprocess


# Note

The mount command is executed using the sudo command, so you may be prompted to enter your password.


SambaTool assumes that the Samba share is using the CIFS protocol. If it is using a different protocol, the mount command may need to be modified.

SambaTool has only been tested on Ubuntu 20.04 LTS. It may not work on other systems or versions of Ubuntu.

