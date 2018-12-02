
class QuadTree:

    def __init__ (self, x, y, width, height, capacity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = [] * capacity
        self.div = [] * 4
        self.isDivided = False
        self.capacity = capacity

    def contains(self, point):
        return (point[0] >= self.x) and (point[0] <= self.x + self.width) and (point[1] <= self.y + self.height) and (point[1] >= self.y)

    def addPoint(self, point):

        if self.isDivided and self.contains(point):
            for tree in self.div:
                if tree.contains(point):
                    tree.addPoint(point)
                    return
        elif (len(self.points) + 1) < self.capacity:
            if self.contains(point):
                self.points.append(point)
        else:
            self.subDivide()

    def getPoints(self, point):
        if self.isDivided:
            for tree in self.div:
                if tree.contains(point):
                    return tree.points
        else:
            return self.points



    def subDivide(self):
        self.isDivided = True
        width = self.width / 2
        height = self.height / 2
        self.div.append(QuadTree(self.x, self.y, width, height,self.capacity))
        self.div.append(QuadTree(self.x + width, self.y, width, height,self.capacity))
        self.div.append(QuadTree(self.x, self.y + height, width, height,self.capacity))
        self.div.append(QuadTree(self.x + width, self.y + height, width, height,self.capacity))
        for point in self.points:
            for tree in self.div:
                tree.addPoint(point)





