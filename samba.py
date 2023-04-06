import os
import subprocess

class SambaTool:
    def __init__(self):
        self.servername = ""
        self.sharename = ""
        self.username = ""
        self.password = ""
        self.mountpoint = ""
        self.domainname = ""
        self.create_mountpoint = False
        self.unmount_after_use = False
        self.mount_options = ""

    def get_user_input(self):
        self.servername = input("Server name: ")
        self.sharename = input("Share name: ")
        self.username = input("Username: ")
        self.password = input("Password: ")
        self.domainname = input("Domain name (leave blank if none): ")
        self.mountpoint = input("Mount point: ")
        self.create_mountpoint = input("Create mount point if it does not exist? (y/n)").lower() == "y"
        self.unmount_after_use = input("Unmount share after use? (y/n)").lower() == "y"
        self.mount_options = input("Additional mount options (leave blank if none): ")

    def mount_share(self):
        # Create mount point directory if it does not exist
        if self.create_mountpoint:
            os.makedirs(self.mountpoint, exist_ok=True)

        # Construct the mount command
        command = [
            "sudo", "mount", "-t", "cifs",
            f"//{self.servername}/{self.sharename}",
            self.mountpoint,
            "-o", f"user={self.username},password={self.password}"
        ]

        # Add domain name to mount options if specified
        if self.domainname:
            command[6] += f",domain={self.domainname}"

        # Add additional mount options if specified
        if self.mount_options:
            command[6] += f",{self.mount_options}"

        # Execute the mount command
        print(f"Mounting {self.servername}/{self.sharename}...")
        result = subprocess.run(command)
        if result.returncode != 0:
            print("Error: mount command failed")
            return

        # Use the mounted share
        print(f"Mounted at {self.mountpoint}")
        # ...

        # Prompt to unmount after use if specified
        if self.unmount_after_use:
            self.unmount_share()

    def unmount_share(self):
        # Unmount the share
        print(f"Unmounting {self.mountpoint}...")
        result = subprocess.run(["sudo", "umount", self.mountpoint])
        if result.returncode != 0:
            print("Error: unmount command failed")
            return

        print("Unmounted.")

# Example usage:
tool = SambaTool()
tool.get_user_input()
tool.mount_share()

# Do something with the mounted share...

# Unmount the share if specified
if tool.unmount_after_use:
    tool.unmount_share()
