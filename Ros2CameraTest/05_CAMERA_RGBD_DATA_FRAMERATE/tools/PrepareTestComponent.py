import azlmbr.legacy.general as general
import azlmbr.bus as bus
import azlmbr.entity as entity
import azlmbr.editor as editor
import azlmbr.entity
import azlmbr.object
from azlmbr.entity import EntityId
from azlmbr.entity import EntityType

import math

def GetDefaultCamera():
    search_filter = entity.SearchFilter()
    search_filter.names = ["Camera"]
    entity_id_list = azlmbr.entity.SearchBus(azlmbr.bus.Broadcast, 'SearchEntities', search_filter)
    assert len(entity_id_list) == 1
    return entity_id_list[0]

if __name__ == "__main__":

    type_name_list = ["ROS2 Camera Sensor", "ROS2 Frame"]
    type_ids_list = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', type_name_list, entity.EntityType().Game)

    ros2_camera_sensor_type_id = type_ids_list[0]

    default_camera_entity = GetDefaultCamera()

    ros_camera_entity_id = azlmbr.editor.ToolsApplicationRequestBus(azlmbr.bus.Broadcast, 'CreateNewEntity', default_camera_entity)
    editor.EditorEntityAPIBus(bus.Event, 'SetName', ros_camera_entity_id, "FooCameraTest")


    azlmbr.components.TransformBus(azlmbr.bus.Event, "SetLocalRotation", ros_camera_entity_id,  azlmbr.math.Vector3(math.radians(-90.0), 0.0, 0.0))

    outcome_ros_camera = editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', ros_camera_entity_id, type_ids_list )
    assert outcome_ros_camera.IsSuccess()
    camera_component_outcome = azlmbr.editor.EditorComponentAPIBus(bus.Broadcast, 'GetComponentOfType', ros_camera_entity_id, ros2_camera_sensor_type_id)
    assert camera_component_outcome.IsSuccess()
    camera_component_id = camera_component_outcome.GetValue()

    path = "Camera configuration|Vertical field of view"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", camera_component_id, path, 90)

    path = "Camera configuration|Image width"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", camera_component_id, path, 350)
    
    path = "Camera configuration|Image height"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", camera_component_id, path, 400)

    path = "Sensor configuration|Frequency"
    editor.EditorComponentAPIBus(bus.Broadcast, "SetComponentProperty", camera_component_id, path, 35)
