from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')

x = 9
y = 8

for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for i in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(y):
            robotArm.moveLeft()    
    else:   
        robotArm.drop()
        robotArm.moveRight()

    y = y - 1
    x = x - 1




robotArm.wait()