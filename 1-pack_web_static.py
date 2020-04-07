#!/usr/bin/python3
"""
Fabric script to create
a .tgz file
"""

import tarfile
import os
from datetime import datetime


def do_pack():
    """ Creates a .tgz archive"""
    target_dir = "versions/"
    file_name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    with tarfile.open(target_dir + file_name, "w:gz") as x:
        x.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(target_dir + file_name):
        return target_dir + file_name
    else:
        return None
