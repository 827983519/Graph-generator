def pp(x):
    """Returns a pretty-print string representation of a number.
       A float number is represented by an integer, if it is whole,
       and up to two decimal places if it isn't
    """
    if isinstance(x, float):
        if x.is_integer():
            return str(int(x))
        else:
            return "{0:.2f}".format(x)
    return str(x)

class point(object):
    """A point in a two dimensional space"""
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '(' + pp(self.x) + ', ' + pp(self.y) + ')'


class line(object):
    """A line between two points"""
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __repr__(self):
        return  str(self.src) + '-->' + str(self.dst)



def intersect (l1, l2):
    """Returns a point at which two lines intersect"""
    x1, y1 = l1.src.x, l1.src.y
    x2, y2 = l1.dst.x, l1.dst.y

    x3, y3 = l2.src.x, l2.src.y
    x4, y4 = l2.dst.x, l2.dst.y

    xnum = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4))
    xden = ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    if xden == 0:
        return -1
    xcoor =  xnum / xden

    ynum = (x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)
    yden = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if yden == 0:
        return -1
    ycoor = ynum / yden

    if x1 >= x2:
        if xcoor < x2 or xcoor > x1:
            return -1
    elif x1 < x2:
        if xcoor < x1 or xcoor > x2:
            return -1
    
    if y1 >= y2:
        if ycoor < y2 or ycoor > x1:
            return -1
    elif y1 < y2:
        if ycoor < y1 or ycoor > y2:
            return -1 

    return point(xcoor, ycoor)


def check_repeat(a,intersection):
    
    if len(intersection) == 0:
        intersection.extend(a)

    else:
        for j in a:
            for i in range(len(intersection)):
                if j.x == intersection[i].x and j.y == intersection[i].y:
                    break
                elif i == len(intersection) - 1:
                    intersection.append(j)
    return intersection
    


def get_intersect(street_line):
    vertics = []
    intersection = []
    for i in range(0,len(street_line) - 1):
        for j in street_line[i]:
            for k in range(i+1,len(street_line)):
                for h in street_line[k]:
                    if intersect(j,h) != -1:
                        vertics = check_repeat([intersect(j,h),h.dst,j.dst,h.src,j.src],vertics) 
                        intersection = check_repeat([intersect(j,h)],intersection) 
                                                            
   
    print intersection
    print vertics
    return vertics




if __name__ == '__main__':
    l1 = line(point(1, 0), point(2, 0))
    l2 = line(point(5, 6), point(3, 8))
    l3 = line(point(1, 5), point(5, 8))

    if intersect(l1,l2) != -1:
        print 'Intersection of', l1, 'with', l2, 'is', intersect(l1, l2)
        print 'Intersection of', l2, 'with', l3, 'is', intersect(l2, l3)
    
    else:
        print "No intersect"