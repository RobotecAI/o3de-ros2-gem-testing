import azlmbr.legacy.general as general
import azlmbr.bus as bus
import azlmbr.entity as entity
import azlmbr.editor as editor
import azlmbr.entity
import azlmbr.object
from azlmbr.entity import EntityId
from azlmbr.entity import EntityType

import subprocess

def GetDefaultCamera():
    search_filter = entity.SearchFilter()
    search_filter.names = ["Camera"]
    entityIdList = azlmbr.entity.SearchBus(azlmbr.bus.Broadcast, 'SearchEntities', search_filter)
    assert len(entityIdList) == 1
    return entityIdList[0]

def CreateOdometry():
    typeNameList = ["ROS2 Wheel Odometry Sensor", "ROS2 Frame", "PhysX Dynamic Rigid Body", "Skid Steering Vehicle Model"]
    typeIdsList = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', typeNameList, entity.EntityType().Game)

    ROS2OdometryType = typeIdsList[0]
    PhysXDynamicRigidBodyType = typeIdsList[2]

    defaultCameraEntity = GetDefaultCamera()

    rosOdometryEntity = azlmbr.editor.ToolsApplicationRequestBus(azlmbr.bus.Broadcast, 'CreateNewEntity', defaultCameraEntity)
    editor.EditorEntityAPIBus(bus.Event, 'SetName', rosOdometryEntity, "TestEntity")


    outcomeROSOdometry = editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', rosOdometryEntity, typeIdsList )
    assert outcomeROSOdometry.IsSuccess()
    outcomeOdometry = azlmbr.editor.EditorComponentAPIBus(bus.Broadcast, 'GetComponentOfType', rosOdometryEntity, ROS2OdometryType)
    assert outcomeOdometry.IsSuccess()
    outcomePhysX = azlmbr.editor.EditorComponentAPIBus(bus.Broadcast, 'GetComponentOfType', rosOdometryEntity, PhysXDynamicRigidBodyType)
    assert outcomePhysX.IsSuccess()

    odometryId = outcomeOdometry.GetValue()
    physxId = outcomePhysX.GetValue()

    path = "Configuration|Gravity enabled"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", physxId, path, False)
    return odometryId

if __name__ == "__main__":
    odometryId = CreateOdometry()
    #general.enter_game_mode()
    #general.idle_wait_frames(1)
    #assert general.is_in_game_mode()
