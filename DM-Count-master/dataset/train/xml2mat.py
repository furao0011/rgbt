import os
import scipy.io as sio
import xml.etree.ElementTree as ET
import glob
import numpy as np


xmls = glob.glob("labels/*.xml")
for xml in xmls:
    tree = ET.parse(xml)
    root = tree.getroot()
    new_root = ET.Element('annotaTion')
    new_tree = ET.Element(new_root)
    arr = []
    for obj in root.findall("object"):
        point = obj.find("point")
        try:
            x=int(point.find("x").text)
            y=int(point.find("y").text)
        except Exception as e:
            print(xml)

        arr.append(np.array([x,y]))
    print(arr)
    sio.savemat(xml.replace("labels","mats").replace("R.xml",".mat"),{"annPoints":np.array(arr)})
