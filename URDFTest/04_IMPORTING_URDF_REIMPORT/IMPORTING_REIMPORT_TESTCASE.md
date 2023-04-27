# Test Goal

 - Check if in the wild URDF reimports

# Test Perquisite

 - Empty default Level
 - ROS2 Gem Activated
 - O3DE Editor running
 - colcon build, git

 Prepare, build ad source workspace

```
mkdir -p testing_ws/src && cd testing_ws/src && \
git clone https://github.com/husky/husky.git && \
cd husky && git checkout 1e0b1d14d657f04ec3a86e73d6676a2cf7af6f79  && \
cd ../.. && colcon build && source install/setup.sh
```
**Do not forget to source your test workspace**
# Steps

## Step 1 

Open URDF importer

### Expected result 

Windows appears

### **Actual RESULT:**

```

```

## Step 2 

Clock "..." and navigate to `testing_ws/src/husky/husky_description/urdf/husky.urdf.xacro`, click Next.

### Expected result 

Step validates.

### **Actual RESULT:**
```

```
## Step 3

Change nothing in `Xacro parameters`
### Expected result 
Step validates, the parameters are shown.

![step3](images/step3.png)


### **Actual RESULT:**
```

```

## Step4

Load assets. Wait for all ticks. One product asset is expected to fail.

### Expected result 
Step validates, all assets (except `bumper.dae`) generated with success.

![step4](images/step4.png)

### **Actual RESULT:**
```

```
## Step5
Create prefab, tick `User articulation for joints and rigid bodies`, close importer

### Expected result 
Step validates, all prefab creation is success.

![step5](images/step5.png)


### **Actual RESULT:**
```

```

## Step 6

Open URDF importer

### Expected result 

Windows appears

### **Actual RESULT:**

```

```

## Step 7 
Click "..." and navigate to `testing_ws/src/husky/husky_description/urdf/husky.urdf.xacro`, click Next.

### Expected result 

Step validates.

### **Actual RESULT:**
```

```
## Step 8

Change nothing in `Xacro parameters`
### Expected result 
Step validates, the parameters are shown.

![step3](images/step3.png)


### **Actual RESULT:**
```

```

## Step 9

Load assets. Wait for all ticks. One product asset is expected to fail.

### Expected result 
Step validates, all assets (except `bumper.dae`) generated with success.

![step4](images/step4.png)

### **Actual RESULT:**
```

```
## Step 10
Create prefab, tick `User articulation for joints and rigid bodies`,
The user should be asked if it is ok to overwrite prefab. Choose `Ok`.

### Expected result 
Step validates, all prefab creation is success.

![step10](images/step10.png)


### **Actual RESULT:**
```

```
