#! /bin/sh

import azlmbr.ROS2
import azlmbr.bus as bus
from pathlib import Path
from azlmbr.entity import EntityId
from azlmbr.entity import EntityType
from azlmbr.components import TransformBus
from azlmbr.math import Vector3

import azlmbr.bus as bus
import azlmbr.legacy.general as general

import xml.etree.ElementTree as ET

def getRobotName(urdfFile):
    # Parse the URDF file
    tree = ET.parse(urdfFile)
    root = tree.getroot()

    # Get the robot name attribute
    robot_name = root.get("name")
    return robot_name

def GetEntity(entityName):
    search_filter = azlmbr.entity.SearchFilter()
    search_filter.names = [entityName]
    entity_id_list = azlmbr.entity.SearchBus(azlmbr.bus.Broadcast, 'SearchEntities', search_filter)
    if (len(entity_id_list)==0):
        return None
    return entity_id_list[0]


ROS2WS_PATH = Path.home() / "testing_ws"
URDF_PATH =  ROS2WS_PATH / "urdfs"

files = []
for file in URDF_PATH.iterdir():
    if file.is_file():
        files.append(str(file))
files.append("/opt/ros/humble/share/moveit_resources_panda_description/urdf/panda.urdf")
files.sort()


def importRobot (urdf):
    fstr = str(urdf)
    robot_name = getRobotName(fstr)
    azlmbr.ROS2.RobotImporterBus(bus.Broadcast, 'ImportURDF', fstr, True, True )

def moveRobot(urdf, locX,locY, locZ):
    fstr = str(urdf)
    robot_name = getRobotName(fstr)
    imported_robot_entity = GetEntity(robot_name)
    new_translation =  azlmbr.math.Vector3(float(locX), float(locY), float(locZ))
    TransformBus(azlmbr.bus.Event, "SetWorldTranslation", imported_robot_entity, new_translation)

def checkCreatedRobot(urdf):
    fstr = str(urdf)
    robot_name = getRobotName(fstr)
    imported_robot_entity = GetEntity(robot_name)
    if imported_robot_entity is None:
        print ("Failed to import urdf {}".format(fstr))
    else:
        print ("Impoted urdf {} as {}".format(fstr, imported_robot_entity) )

# tickNo = 0

for urdfName in files:
    importRobot(urdfName)

handler = bus.NotificationHandler('TickBus')


def onTick(args):
    for i,urdfName in enumerate(files):
        moveRobot(urdfName,0,i,0)
        checkCreatedRobot(urdfName)
    handler.disconnect()

handler.connect()
handler.add_callback('OnTick', onTick)

