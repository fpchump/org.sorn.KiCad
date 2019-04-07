# -*- coding: utf-8 -*-

"""A script use for export all KiCad programs, so that they will have correct
menu item and icon outside the program protected environment.

Basically, it just copy original icons/desktop files and prefix them with
project id and fix icon name in desktop files.

"""


import os
import io
import glob
import os.path
import shutil


def main():
    apps = [
        "bitmap2component",
        "gerbview",
        "pcbcalculator",
        "eeschema",
        "pcbnew",
    ]

    app_id = "org.sorn.KiCad"

    # Export all directories
    export_dirs = ["/app/share/applications", "/app/share/icons"]
    for export_dir in export_dirs:
        for root, dirs, files in os.walk(export_dir):
            for afile in files:
                for app_name in apps:
                    name, ext = os.path.splitext(afile)
                    if app_name == name:
                        src_path = os.path.join(root, afile)
                        dst_path = os.path.join(
                            root, "%s.%s" % (app_id, afile)
                        )

                        print("Copy %s to %s" % (src_path, dst_path))

                        # Fixs desktop file icons:
                        if ".desktop" == ext:
                            print("Fixs icons in desktop file.")

                            src_file = io.open(src_path, "r", encoding="utf-8")
                            dst_file = io.open(dst_path, "w", encoding="utf-8")
                            try:
                                dst_file.write(
                                    src_file.read().replace(
                                        "Icon=%s" % app_name,
                                        "Icon=%s.%s" % (app_id, app_name),
                                    )
                                )
                            finally:
                                dst_file.close()
                                src_file.close()
                        else:
                            shutil.copyfile(src_path, dst_path)


if __name__ == "__main__":
    main()
