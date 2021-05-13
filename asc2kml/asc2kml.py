import os

import oneAsc2kml

def asc2kml(ascfilesdir):
    ascfilesList = os.listdir(ascfilesdir)

    for ascfile in ascfilesList: 
        if os.path.splitext(ascfile)[1] == ".ASC":
            bestgnsspos_asc_dir = ascfilesdir + "/" + ascfile 
            oneAsc2kml.oneAsc2kml(bestgnsspos_asc_dir)

#test...
# folder of bestgnsspos.asc
# ascfilesdir = "/home/slam/EcarxTools_202102/asc2kml"
# asc2kml(ascfilesdir)