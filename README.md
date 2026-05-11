# Landmine Detection Robot using ROS2 and Gazebo

## Overview

This project is a robotics simulation developed during my M1 Artificial Intelligence studies.

It simulates an autonomous mobile robot navigating a warzone-like environment, avoiding obstacles, building a map, and detecting underground landmines.

The project uses **ROS2** as the robotics middleware and **Gazebo** as the simulation environment. The robot is equipped with simulated sensors such as **LiDAR**, a **metallic sensor**, and a custom **GPR-style detection node** to identify hidden landmines.

## Project Objective

The main objective of this project is to simulate how an autonomous robot can assist in dangerous missions by exploring unknown environments and detecting possible landmine locations without putting humans at risk.

The project focuses on:

- Autonomous robot navigation
- Obstacle avoidance
- Environment simulation
- Landmine detection
- SLAM and mapping
- Sensor-based robotic behavior
- Visualization using RViz

## Project Motivation

Landmine detection is a dangerous task in real-world environments. Sending humans into these zones can be risky and unsafe.

This project explores how robotics and simulation can be used to design safer solutions. By using a simulated robot, we can test navigation, obstacle avoidance, and underground mine detection in a controlled virtual environment.

Although this project is simulation-based, it represents an important real-world use case of robotics, autonomous systems, and AI for humanitarian and safety applications.

## Main Features

- ROS2-based robotics system
- Gazebo simulation environment
- TurtleBot3 mobile robot simulation
- Custom warzone-like environment
- LiDAR-based obstacle detection
- Obstacle avoidance behavior
- Simulated Ground Penetrating Radar detection logic
- Simulated metallic sensor logic
- Landmine detection based on robot position
- SLAM and map visualization using RViz
- Custom ROS2 launch files
- Custom Gazebo worlds and models

## Technologies Used

- Ubuntu
- ROS2 Humble
- Gazebo
- TurtleBot3
- Python
- RViz
- Cartographer SLAM
- ROS2 Python nodes
- Gazebo world files

## System Architecture

The system is composed of several ROS2 nodes and simulation components working together.

```txt
Gazebo Simulation Environment
        |
        v
TurtleBot3 Mobile Robot
        |
        v
LiDAR Sensor --------------> Obstacle Avoidance Node
        |
        v
Odometry Data -------------> GPR Landmine Detection Node
        |
        v
Metallic Sensor Node ------> Mine Detection Logic
        |
        v
Detected Mine Locations
        |
        v
RViz / Map Visualization
```

## How the System Works

The robot starts inside a simulated warzone environment created in Gazebo.

First, the robot uses its LiDAR sensor to detect obstacles around it. The obstacle avoidance node processes the LiDAR data and helps the robot move safely without colliding with objects.

At the same time, the robot’s position is tracked using odometry data. The custom GPR-style detection node reads the robot position and compares it with predefined landmine coordinates.

When the robot gets close to a landmine location, the system detects the mine and reports its position. The metallic sensor node can also be used as an additional simulated detection layer.

The results can be visualized using RViz, where the user can observe the robot movement, LiDAR scans, generated map, and detected danger zones.

## Project Structure

```txt
landmine-detection-robot/
│
├── landmine_robot/
│   ├── landmine_robot/
│   │   ├── avoidance.py
│   │   ├── gpr.py
│   │   └── metallic_sensor.py
│   ├── package.xml
│   ├── setup.py
│   └── resource/
│
├── my_tb3_launch/
│   ├── launch/
│   ├── config/
│   └── worlds/
│
├── warzone_sim/
│   ├── launch/
│   ├── worlds/
│   └── models/
│
├── README.md
└── .gitignore
```

## Main Components

### 1. Gazebo Simulation

Gazebo is used to create and run the virtual environment.

The simulation includes the robot, obstacles, and the warzone-like world where landmines are placed.

### 2. TurtleBot3 Robot

TurtleBot3 is used as the mobile robot platform.

The robot moves inside the environment and collects sensor data while navigating.

### 3. LiDAR Sensor

The LiDAR sensor provides distance measurements around the robot.

This data is used to detect obstacles and avoid collisions.

### 4. Obstacle Avoidance Node

The obstacle avoidance node reads LiDAR data and controls the robot movement.

If an obstacle is detected, the robot changes direction to avoid it.

### 5. GPR Detection Node

The GPR detection node simulates Ground Penetrating Radar behavior.

It uses the robot’s odometry position and compares it with predefined mine coordinates.

If the robot gets close enough to a mine, the node detects it and reports the location.

### 6. Metallic Sensor Node

The metallic sensor node simulates an additional mine detection sensor.

It supports the detection logic by representing how metallic objects could be identified underground.

### 7. SLAM and RViz Visualization

SLAM is used to build a map of the environment while the robot moves.

RViz is used to visualize the robot, LiDAR scans, generated map, and detected mine positions.

## How to Run the Project

### 1. Go to your ROS2 workspace

```bash
cd ~/ros2_ws
```

### 2. Build the workspace

```bash
colcon build
```

### 3. Source the workspace

```bash
source install/setup.bash
```

### 4. Set the TurtleBot3 model

```bash
export TURTLEBOT3_MODEL=burger
```

### 5. Launch the simulation

Depending on your launch file, run one of the following commands:

```bash
ros2 launch my_tb3_launch warzone.launch.py
```

or:

```bash
ros2 launch warzone_sim gazebo.launch.py
```

### 6. Run the obstacle avoidance node

```bash
ros2 run landmine_robot avoidance
```

### 7. Run the GPR detection node

```bash
ros2 run landmine_robot gpr
```

### 8. Run the metallic sensor node

```bash
ros2 run landmine_robot metallic_sensor
```

## Running SLAM

To run Cartographer SLAM with TurtleBot3:

```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```

RViz can be used to visualize:

- Robot position
- LiDAR scans
- Map generation
- Obstacle detection
- Detected mine locations
- Robot navigation behavior

## Example Use Case

The robot is placed in a dangerous simulated environment.

It starts moving and scanning the area using LiDAR. When it finds obstacles, it avoids them.

While moving, the robot continuously checks its position using odometry.

If it reaches an area close to a predefined mine coordinate, the GPR node detects the mine and reports it.

This simulates how a robot could help identify dangerous underground objects before humans enter the area.

## What I Learned

Through this project, I practiced:

- Creating ROS2 packages
- Writing ROS2 Python nodes
- Working with Gazebo simulations
- Using TurtleBot3 in simulation
- Reading LiDAR sensor data
- Implementing obstacle avoidance
- Using odometry data
- Simulating landmine detection logic
- Creating custom Gazebo worlds
- Using launch files in ROS2
- Visualizing robotic systems in RViz
- Understanding SLAM and mapping concepts

## Challenges Faced

During the project, several challenges were encountered, including:

- Setting up ROS2 and Gazebo correctly
- Launching custom Gazebo worlds
- Connecting TurtleBot3 with the simulation environment
- Managing ROS2 packages and entry points
- Debugging node execution errors
- Working with odometry and robot position
- Visualizing detected mines on maps
- Understanding costmaps and SLAM integration

These challenges helped improve my understanding of robotic systems and ROS2 development.

## Future Improvements

Possible future improvements include:

- Improve mine visualization on the map
- Add better costmap integration
- Add autonomous path planning
- Use Navigation2 for advanced navigation
- Add more realistic GPR signal simulation
- Add multiple types of landmines
- Improve the warzone environment design
- Add a dashboard for monitoring detected mines
- Add logs for detected mine positions
- Deploy the project with a more complete robot navigation pipeline

## Repository Purpose

This repository is part of my academic and personal portfolio.

It showcases my work in:

- Robotics simulation
- ROS2 development
- Gazebo environments
- Autonomous navigation
- Obstacle avoidance
- Sensor-based detection
- SLAM and visualization

## Author

**Giovanni Da Silva Ghoul**  
Master’s Student in Artificial Intelligence  
Université Saint-Joseph de Beyrouth

## License

This project is for academic and educational purposes.
