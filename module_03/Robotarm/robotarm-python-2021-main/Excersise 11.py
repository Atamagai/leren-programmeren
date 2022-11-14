from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')

for i in range(8):
    robotArm.moveRight()
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        for i in range(2):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
robotArm.wait()