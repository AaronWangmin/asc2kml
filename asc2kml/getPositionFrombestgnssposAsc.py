import os
from os.path import expanduser

def getPositionFrombestgnssposAsc(bestgnssposAsc_dir):
    
    BLH = []

    ascFile = open(bestgnssposAsc_dir, "r")

    for lineStr in ascFile.readlines():        
         value = lineStr.split(",")
         positionStr = value[12] + "," + value[11] + "," + value[13] + "\n"
         BLH.append(positionStr)              

    ascFile.close()

    return BLH


# test...

# bestgnsspos_asc_dir = "/home/slam/EcarxTools_202102/asc2kml/20210428171628_WANGMIN_SHANGHAI_AF22091.asc"
# BLH = getPositionFrombestgnssposAsc(bestgnsspos_asc_dir)
# print("hell")
