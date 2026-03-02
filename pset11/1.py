class vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class vector3D(vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def show(self):
        print(f"3D Vector: {self.x}i + {self.y}j + {self.z}k")

a,b,c = map(int, input("Enter values: ").split())
v3 = vector3D(a,b,c)
v3.show()