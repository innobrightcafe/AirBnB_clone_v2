#!/usr/bin/python3
#A Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack
import os
import tarfile
from datetime import datetime

def do_pack():
    #Define the current timestamp in the format of year-month-day_hour-minute-second
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f"archive_{timestamp}.tgz"
    dir_to_archive = "../AirBnB_clone_v2/web_static"
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(dir_to_archive)     
     if os.path.exists(archive_name):
        return archive_name
    else:
        return None
