# Test Goal

 - Check if ROS2 Camera sensor is configuration is saved and loaded correctly.

# Test Perquisite

 - Empty, fresh default Level
 - ROS2 Gem Activated
 - O3DE Editor running

# Steps

## Step 1 

### 

Execute preparation script in o3de console:
```
pyRunFile Ros2CameraTest/04_CAMERA_RGBD_DATA_FRAMERATE/tools/PrepareTestComponent.py
```

### Expected result 

- Script finishes, camera is created : 

- `FooCameraTest` entity creates
- `FooCameraTest` has two activated components : `ROS2 Frame`, `ROS2 Camera Sensor`

### **Actual RESULT:**

```

```
## Step 2

Start simulation with CTRL+G

### Expected result 
No warnings, simulation running at least 60 FPS
### **Actual RESULT:**

```

```

## Step 3

Verify framerate (bash command):
```bash
timeout  -s 9 3  ros2 topic hz -s /FooCameraTest/camera_image_color

```
### Expected result 
```
average rate: 19.697
	min: 0.049s max: 0.066s std dev: 0.00338s window: 21
average rate: 19.842
	min: 0.049s max: 0.066s std dev: 0.00246s window: 41
Killed
```
**Small variations are acceptable**
### **Actual RESULT:**

```

```

## Step 4

Verify framerate:
```bash
timeout  -s 9 3  ros2 topic hz -s /FooCameraTest/camera_image_depth

```
### Expected result 
```
average rate: 19.697
	min: 0.049s max: 0.066s std dev: 0.00338s window: 21
average rate: 19.842
	min: 0.049s max: 0.066s std dev: 0.00246s window: 41
Killed
```
**Small variations are acceptable**
### **Actual RESULT:**

```

```

## Step 5

Verify framerate:
```bash
timeout  -s 9 3  ros2 topic hz -s /FooCameraTest/color_camera_info

```
### Expected result 
```
average rate: 19.997
	min: 0.046s max: 0.054s std dev: 0.00134s window: 21
average rate: 19.996
	min: 0.022s max: 0.078s std dev: 0.00617s window: 41
Killed
```
**Small variations are acceptable**
### **Actual RESULT:**

```

```

## Step 5

Verify framerate:
```bash
timeout  -s 9 3  ros2 topic hz -s /FooCameraTest/depth_camera_info

```
### Expected result 
```
average rate: 20.006
	min: 0.046s max: 0.054s std dev: 0.00109s window: 22
average rate: 20.002
	min: 0.046s max: 0.054s std dev: 0.00080s window: 42
Killed
```
**Small variations are acceptable**
### **Actual RESULT:**

```

```
