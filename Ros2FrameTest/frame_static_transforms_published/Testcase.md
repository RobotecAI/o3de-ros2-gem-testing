## Test Goal

Check if the prefab with defined tf tree is loaded correctly and the transforms are published.

## Test Perquisites

- Empty default Level
- ROS2 Gem Activated
- O3DE Editor running

## Steps

1. Add the prefab to the level by right clicking on the level then `Instantiate Prefab` and select the prefab `ROSbot.prefab`
![add prefab](asset/add-prefab.png)
2. Run the script for checking the `tf_static` by running the command `python3 tools/check_tf_static.py`  
3. Run the game (`ctrl + G`)
4. Check the `tf_static` by running the command `ros2 topic echo /tf_static` This should print the transform between the two frames. Move the camera (WASD) and check if the transform is updated.

## Expected Result

The prefab is loaded and transforms are published. No duplicate in parent-child relationship in the tf tree.