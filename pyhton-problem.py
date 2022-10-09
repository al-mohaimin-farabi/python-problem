class Point():

    x = 0
    y = 0
    speed = 1
    listOne = [0, 0]

    def __setattr__(self, key, value):
        print(key, value)
        if self.x <= -2 or self.x >= 2:
            self.printPoint(" Beyond Boundary!")
            exit()

        elif self.y >= 3 or self.y <= -3:
            self.printPoint(" Beyond Boundary!")
            exit()

        self.__dict__[key] = value

    def left(self):
        self.x -= self.speed
        if self.x < -2:
            return
        else:
            self.listOne.append(self.x)
            self.listOne.append(self.y)

    def right(self):
        self.x += self.speed
        if self.x > 2:
            return
        else:
            self.listOne.append(self.x)
            self.listOne.append(self.y)

    def up(self):
        self.y += self.speed
        if self.y > 3:
            return
        else:
            self.listOne.append(self.x)
            self.listOne.append(self.y)

    def down(self):
        self.y -= self.speed
        if self.y < -3:
            return
        else:
            self.listOne.append(self.x)
            self.listOne.append(self.y)

    def printPoint(self, range):

        lst = str(list(zip(self.listOne[::2], self.listOne[1::2]))).replace(
            '), (', ')(')
        res = str(lst)[1:-1]
        if range == " Beyond Boundary!":
            print(res.replace(" ", "")+range)
        else:
            print(res.replace(" ", ""))

# try:


def main():
    P = Point()
    UserIn = str(input("Directions? "))
    for i in UserIn:
        if i.lower() == 'l':
            P.left()
        elif i.lower() == 'r':
            P.right()
        elif i.lower() == 'u':
            P.up()
        elif i.lower() == 'd':
            P.down()
    P.printPoint("")


main()

# except TypeError:
#     print("Some Error Happend")
