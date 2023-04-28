## Change Lidar Implementation to RGL

### Objective: Ensure that Lidar Component can switch to RGL implementation and observe GPU calculations performance benefits

### Prerequisites:

- O3DE Editor is running and the scene is already opened.
- ROS2 Gem and RGL Gem are enabled for the project
- A scene has been created in the O3DE Editor.
- A robot prefab has been imported into the scene and it already has a Lidar component added to it.
- The RGL Gem has been registered and enabled in the project.

### Test Steps:

1. With the Lidar component selected in the Entity Inspector, locate the "Lidar Implementation" dropdown and select "RGL".
2. Increase the number of layers to a higher value (e.g., 64) and points per layer (e.g., 2048) in the Lidar component parameters.
3. Click the "Play" button in the top toolbar to enter Game mode and observe the FPS.
4. Exit Game mode by pressing `ESC` or clicking the "Stop" button.
5. Change the "Lidar Implementation" dropdown to another implementation (e.g., "Default").
6. Click the "Play" button in the top toolbar to enter Game mode and observe the FPS.
7. Compare the FPS between the RGL and the other implementation.

### Expected Result:

The Lidar component should be able to switch to the RGL implementation, and the GPU calculations performance benefits should be observed. When using the RGL implementation, the FPS in Game mode should be significantly higher compared to the other implementation, especially when using a higher number of layers and points per layer.