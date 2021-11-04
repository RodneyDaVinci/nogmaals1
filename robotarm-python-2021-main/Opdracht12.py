from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

for i in range(0,8):
    robotArm.moveRight()

for i in range(1,9):
    robotArm.grab()
    scan = robotArm.scan()

    if scan == "red":
        for c in range(0,i):
            robotArm.moveRight()
            
        robotArm.drop() 

        for c in range(0,i):
            robotArm.moveLeft()  
    else:
        robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()