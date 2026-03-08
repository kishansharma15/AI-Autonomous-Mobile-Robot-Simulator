# AI Autonomous Mobile Robot Simulator

The aim of this project is to create an AI-based Autonomous Mobile Robot (AMR) Simulator. 

The main features of the robot are:

* Path Planning use the A* algorithm
* Obstacle avoidance
* Dead-reckoning localization
* Kalman filter-based localization
* Particle filter-based localization
* SLAM mapping
* PID motor control

The robot will move around in a grid and avoid obstacles while estimating its own location.

## Used Technologies

* Python
* Numpy
* Matplotlib

## To Run

1. Install the dependencies `pip install -r requirements.txt`

2. Run the simulator `python main.py`