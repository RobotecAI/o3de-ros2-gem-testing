import azlmbr.legacy.general as general
import azlmbr.bus as bus
import azlmbr.entity as entity
import azlmbr.editor as editor
import azlmbr.entity
import azlmbr.object
from azlmbr.entity import EntityId
from azlmbr.entity import EntityType

import subprocess
DEGREE_RADIAN_FACTOR = 0.0174533

def GetDefaultCamera():
    search_filter = entity.SearchFilter()
    search_filter.names = ["Camera"]
    entityIdList = azlmbr.entity.SearchBus(azlmbr.bus.Broadcast, 'SearchEntities', search_filter)
    assert len(entityIdList) == 1
    return entityIdList[0]

if __name__ == "__main__":

    typeNameList = ["ROS2 Camera Sensor", "ROS2 Frame"]
    typeIdsList = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', typeNameList, entity.EntityType().Game)

    ROS2CameraSensorTypeId = typeIdsList[0]

    defaultCameraEntity = GetDefaultCamera()

    rosCameraEntityId = azlmbr.editor.ToolsApplicationRequestBus(azlmbr.bus.Broadcast, 'CreateNewEntity', defaultCameraEntity)
    editor.EditorEntityAPIBus(bus.Event, 'SetName', rosCameraEntityId, "FooCameraTest")


    azlmbr.components.TransformBus(azlmbr.bus.Event, "SetLocalRotation", rosCameraEntityId,  azlmbr.math.Vector3(-DEGREE_RADIAN_FACTOR*90.0, 0.0, 0.0))

    outcomeROS2Camera = editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', rosCameraEntityId, typeIdsList )
    assert outcomeROS2Camera.IsSuccess()
    cameraComponentOutcome = azlmbr.editor.EditorComponentAPIBus(bus.Broadcast, 'GetComponentOfType', rosCameraEntityId, ROS2CameraSensorTypeId)
    assert cameraComponentOutcome.IsSuccess()
    cameraComponentId = cameraComponentOutcome.GetValue()

    path = "Camera configuration|Vertical field of view"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", cameraComponentId, path, 90)

    path = "Camera configuration|Image width"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", cameraComponentId, path, 350)
    
    path = "Camera configuration|Image height"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", cameraComponentId, path, 400)

    path = "Sensor configuration|Frequency"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", cameraComponentId, path, 35)


