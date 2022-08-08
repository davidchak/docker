from importlib.metadata import packages_distributions
import os

packages_to_install = [
    "nginx-ssl-util",
    "nginx",
    "nginx-mod-luci",
    "nginx-ssl",
    "uwsgi",
    "uwsgi-luci-support"
]

os.system("opkg update")

for package in packages_to_install:
    os.system(f"opkg install {package}")