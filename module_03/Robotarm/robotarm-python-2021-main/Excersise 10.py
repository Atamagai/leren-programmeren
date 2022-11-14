from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
x = 9
y = 8
for i in range (5):
    robotArm.grab()
    for i in range(x):
        robotArm.moveRight()
    x = x - 2
    robotArm.drop()
    for i in range(y):
        robotArm.moveLeft()
    y = y - 2 
robotArm.wait()