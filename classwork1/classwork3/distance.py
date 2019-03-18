import math

class Point:
    """Represents a point in a 2D space"""
    pass

def distance_between_points(p1,p2):
    """Calculate distance between two points"""
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)

if __name__ == '__main__':
    blank1=Point()
    blank2=Point()

    blank1.x=3
    blank1.y=7
    blank2.x=2
    blank2.y=33
     
     
    dist=distance_between_points(blank1,blank2)
    print(f'distance is', dist)