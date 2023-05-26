## Test Goal

Check when the frame is added to the tf tree the transform is published

## Test Perquisites

- Empty default Level
- ROS2 Gem Activated
- O3DE Editor running 

## Steps 

- Create entity

- Create second entity (child of the first entity)

- Add the frame component to the both entities, the hierarchy should look like this:

![entities](asset/entities.png)

- Set the name to "sensor_frame2", should look like this:

![entity 2 frame name](asset/entity2-frame.png)

- Run the game (`ctrl + G`) 

- Check if the frame is added to the tf tree `ros2 run tf2_tools view_frames` This will create a file `*.pdf` in the current directory it should contain the following frames:

![tf tree](asset/frames-hierarchy.png)
