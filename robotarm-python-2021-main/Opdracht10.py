from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

for i in range(5):
    robotArm.grab()

    for a in range(9-(2*i)):
        robotArm.moveRight()
    print(a)
    robotArm.drop()

    for b in range(8-(2*i)):
        robotArm.moveLeft()
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()