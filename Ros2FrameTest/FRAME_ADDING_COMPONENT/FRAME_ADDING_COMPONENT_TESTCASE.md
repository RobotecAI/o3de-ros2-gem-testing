## Test Goal 

Check if the frame is added to the tf tree.

## Test Perquisites

- Empty default Level
- ROS2 Gem Activated
- O3DE Editor running

## Steps

- Create entity

![add entity](asset/add-entity.png)

- Check if there are no frames in the tf tree `ros2 run tf2_tools view_frames` This will create a file `*.pdf` in the current directory it should contain the following frames:
![tf tree empty](asset/frames-no-tf.png)

- Add the frame component to the entity

![add component](asset/add-ros2-frame.png)

- The component should look like this:

![result](asset/resulting.png)

- Check if the frame is added to the tf tree `ros2 run tf2_tools view_frames` This will create a file `*.pdf` in the current directory it should contain the following frames:

![tf tree](asset/frames-tf-present.png) 