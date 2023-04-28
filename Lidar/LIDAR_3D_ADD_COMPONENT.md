## Add Lidar 3D Component

### Objective: Ensure that Lidar 3D Component can be added to the scene

### Prerequisites:

- O3DE Editor is running and the scene is already opened.
- ROS2 Gem is enabled for the project
- A scene has been created in the O3DE Editor.
- A robot prefab has been imported into the scene.

### Test Steps:

1. Create the entity in the prefab instance that will represent Lidar.
2. With the entity selected, go to the `Entity Inspector` panel and click on the `Add Component` button.
3. Select `ROS2 Lidar 3D Sensor` from the list of available components.
4. Note there is a required component missing and the newly added component is grayed out. Click `Add Required Component` to add the `ROS2 Frame` component to the entity.
5. In the component's properties panel, adjust the desired parameters for the Lidar sensor, and ensure `Visualise` property is toggled on.
6. Add a simple object with the `PhysX Collider` component and drag it to the scene viewport in a range of the robot's Lidar.
7. Switch to Game mode by clicking the Play button on the top toolbar (`Ctrl+G`).
8. In Game mode, verify that the Lidar component is detecting the object with the PhysX Collider component and rendering the collision data points in the scene viewport.

### Expected Result:

The Lidar component should be successfully added to the robot prefab, and the Lidar sensor should be able to detect other objects in the scene when in Game mode, with the data rendered in the scene viewport.

