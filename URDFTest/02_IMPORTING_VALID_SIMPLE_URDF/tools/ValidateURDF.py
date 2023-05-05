import azlmbr.legacy.general as general
import azlmbr.bus as bus
import azlmbr.entity as entity
import azlmbr.editor as editor
import azlmbr.entity
import azlmbr.object
from azlmbr.entity import EntityId
from azlmbr.entity import EntityType


def GetEntityWithName(entityName):
    search_filter = entity.SearchFilter()
    search_filter.names = [entityName]
    entity_id_list = azlmbr.entity.SearchBus(azlmbr.bus.Broadcast, 'SearchEntities', search_filter)
    assert len(entity_id_list) == 1
    return entity_id_list[0]

def CheckIfEntityHasTypeComponents (entityId, type_name_list):
    type_ids_list = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', type_name_list, entity.EntityType().Game)
    for [componentTypeName, componentType] in zip(type_name_list, type_ids_list):
            outcome = azlmbr.editor.EditorComponentAPIBus(bus.Broadcast, 'GetComponentOfType', entityId,componentType)

            isActive = False
            if (outcome is not None and outcome.isSuccess()):
                isActive = azlmbr.editor.EditorComponentAPIBus(bus.Broadcast, 'IsComponentEnabled', outcome.GetValue())

            print (f"Component {componentTypeName} : {outcome.isSuccess()}, active :{isActive}")
            assert outcome.isSuccess()
            assert isActive


if __name__ == "__main__":
    print ("Test box_link")
    box_link_id = GetEntityWithName("box_link")
    CheckIfEntityHasTypeComponents(box_link_id, ["ROS2 Frame", "PhysX Dynamic Rigid Body", "PhysX Primitive Collider"])

    print ("Test suzanne_link")
    suzanne_link_id = GetEntityWithName("suzanne_link")
    CheckIfEntityHasTypeComponents(suzanne_link_id, ["ROS2 Frame", "PhysX Dynamic Rigid Body", "PhysX Fixed Joint", "PhysX Mesh Collider"])

    print ("Test suzanne_link_visual")
    suzanne_link_visual_id = GetEntityWithName("suzanne_link_visual")
    CheckIfEntityHasTypeComponents(suzanne_link_visual_id, ["Mesh"])
