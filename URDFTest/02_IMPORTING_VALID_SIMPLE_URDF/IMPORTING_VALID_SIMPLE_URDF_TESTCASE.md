# Test Goal

 - Check if simple URDF is imported

# Test Perquisite

 - Empty default Level
 - ROS2 Gem Activated
 - O3DE Editor running

# Steps

## Step 1 

Open URDF importer

### Expected result 

Windows appears

![step1](images/step1.png)

### **Actual RESULT:**

```

```

## Step 2

- Click next, choose file with "..." button.
- Navigate to attached `data` directory
- Pick `chain.urdf`
- Click `OK` 
- Click `Next`

### Expected result 
Wizard Page validate, next page was loaded.

![step1](images/step2.png)

### **Actual RESULT:**
```

```

## Step 3
Validate is assets are processed correctly

### Expected result 
All assets were processed.

![step1](images/step3.png)

### **Actual RESULT:**

```

```
## Step 4
Create prefab

### Expected result 
The prefab is created and reported:

![step1](images/step4.png)

### **Actual RESULT:**

```

```

## Step 5

Veritfy if:
- all shapes are created
- Suzanne monkey has collider

**please make sure that "Show Helpers for all Entities" is chosen**
### Expected result 
all shapes are drown, monkey has visible mesh and collider.
![step6](images/step5.png)

### **Actual RESULT:**

```

```

## Step 6 

Run verification script
```
pyRunFile /home/michal/o3de-ros2-gem-testing/URFTest/02_IMPORTING_VALID_SIMPLE_URDF/tools/ValidateURDF.py
```
### Expected result 
Script succeed:

![step6](images/step6.png)

### **Actual RESULT:**

```

```