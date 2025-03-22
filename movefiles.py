import shutil
import os

# Check if the destination folder exists, if not, create it
def move_allfiles(origin,destination,file):

    # Move the file from the source folder to the destination folder
        path_origin = os.path.join(origin, file)
        path_destination = os.path.join(destination, file)

        if os.path.isfile(path_origin):  # Check if it is a file
            shutil.move(path_origin, path_destination)