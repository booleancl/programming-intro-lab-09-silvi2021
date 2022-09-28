class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_to(self,other_point):
        distance_x = self.x - other_point.x
        distance_y = self.y - other_point.y

        distance = (distance_x**2 + distance_y**2)**(1/2)
        return distance
        


    
