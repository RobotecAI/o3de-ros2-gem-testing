## Test Goal

Check if the changing of the namespace in the frame component is reflected in the tf tree.

## Test Perquisites

- Empty default Level
- ROS2 Gem Activated
- O3DE Editor running

## Steps

- Create entity

- Add the frame component to the entity the tf frames without changing the namespace.

- Run the game (`ctrl + G`)

- Check the frames by running `ros2 run tf2_tools view_frames`. The frame component should look like this:

![frames without namespace](asset/frames-without-namespace.png)

- Stop the game (`Esc Esc`) and add the namespace `test_namespace` to the frame component.

![add namespace](asset/add-custom-namespace.png)

- Run the game (`ctrl + G`)

- Check the frames by running `ros2 run tf2_tools view_frames`. The frame component should look like this:

![frames with namespace](asset/frames-with-namespace.png)