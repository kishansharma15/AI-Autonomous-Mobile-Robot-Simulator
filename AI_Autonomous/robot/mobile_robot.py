class MobileRobot:

    def __init__(self,start):

        self.x = start[0]
        self.y = start[1]

    def move(self,step):

        self.x = step[0]
        self.y = step[1]

        print("Robot moved to:",self.x,self.y)