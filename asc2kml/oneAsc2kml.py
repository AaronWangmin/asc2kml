import os
import getPositionFrombestgnssposAsc


def oneAsc2kml(bestgnsspos_asc_dir):
  # bestgnsspos_asc_dir = "/home/slam/EcarxTools_202102/asc2kml/20210428171628_WANGMIN_SHANGHAI_AF22091.asc"
  dirname = os.path.splitext(bestgnsspos_asc_dir)[0]
  basename = os.path.splitext(bestgnsspos_asc_dir)[1]

  # kml path
  kmlPath = dirname + ".kml"

  # kml child node: name
  name = os.path.split(dirname)[1]

  # get coordinates
  coordinates = getPositionFrombestgnssposAsc.getPositionFrombestgnssposAsc(bestgnsspos_asc_dir)

  #create kml file 
  kmlPathFile = open(kmlPath,"w+")

  # header of xml
  kmlPathFile.write('''<?xml version="1.0" encoding="UTF-8"?> \n''')
  kmlPathFile.write('''<kml>
      <Document>
          <Placemark> \n''')

  # name
  kmlPathFile.write("         <name>" + name + "</name> \n")

  # kml line define
  kmlPathFile.write('''           <visibility>1</visibility>
              <LineString>
              <altitudeMode>clampToGround</altitudeMode>
              <coordinates> \n''')

  # coordinate
  kmlPathFile.writelines(coordinates)

  # kml tail
  kmlPathFile.write('''
          </coordinates>
        </LineString>
      </Placemark>
    </Document>
  </kml>''')

  kmlPathFile.close

# test....
# bestgnsspos_asc_dir = "/home/slam/EcarxTools_202102/asc2kml/20210428171628_WANGMIN_SHANGHAI_AF22091.asc"
# oneAsc2kml(bestgnsspos_asc_dir)
# print("dirname:" + dirname)
# print("basename:" + basename)
