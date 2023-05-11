from printer.models import Settings
# import argparse

import subprocess as sp

# parser = argparse.ArgumentParser(
#                     prog='printer-gui',
#                     description='Django web app for RPi to handle print jobs using a connected CUPS printer.')

# parser.add_argument('-r', '--raspberry', action='store_true')      # option that takes a value
# parser.add_argument('-n', '--name')  # on/off flag

# args = parser.parse_args()

raspi_commands = [
    'sudo apt install -y cups',
    'sudo apt install -y default-jre libreoffice-core libreoffice-common libreoffice-java-common',
    'sudo apt install -y --no-install-recommends libreoffice-writer libreoffice-gtk3',
    'sudo usermod -aG lpadmin pi'
]

migrations_commands = [
    'python manage.py makemigrations printer --skip-checks',
    'python manage.py migrate --skip-checks'
]

print("\n================== printer-gui ==================")
print("Author: Ryan Haas (github.com/haasr/printer-gui)")
print("=================================================\n")

# if args.rasberry:
if False:
    print("\n------------------------------------")
    print("Installing Aptitude dependencies...")
    for cmd in raspi_commands:
        print(f">> \033[93m {cmd}\033[00m")
        resp = sp.call(cmd, shell=True)
        if resp == 0:
            print(f"\033[92m[ ✓ OK ]\033[00m")
        else:
            print(f"\033[91m[ X Failed! ]\033 ]00m")

print("\n------------------------------------")
print("Migrating the database...")

for cmd in migrations_commands:
    print(f">> \033[93m {cmd}\033[00m")
    resp = sp.call(cmd, shell=True)
    if resp == 0:
        print(f"\033[92m[ ✓ OK ]\033[00m")
    else:
        print(f"\033[91m[ X Failed! ]\033 ]00m")

print("\n------------------------------------")

app_title='GUI Print Server'

# if args.name : app_title = args.name

x = Settings(
    id=1,
    app_title=app_title,
    default_color='RGB',
    default_orientation='3',
    printer_profile='None found'
)
x.save()

print(f"\033[92m[ DONE ]\033[00m")
print("Type \033[93mexit()\033[00m to exit the shell")