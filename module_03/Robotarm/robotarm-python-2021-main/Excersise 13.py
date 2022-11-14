from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

y = 1
x = 1

for i in range (7):
    robotArm.grab()
    colour = robotArm.scan()
    if colour == "":
        quit()
    else:
        for i in range(x):
            robotArm.moveRight()
        robotArm.drop()
    for i  in range (y):
        robotArm.moveLeft()        

    x = x + 1
    y = y + 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()