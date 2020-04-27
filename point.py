from ecommerce import shipping
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("draw")


point = Point(10, 23)
point.draw()
print(point.x)
shipping. calc_shipping()

print(random.randint(1, 6))
members = ["Rishabh", "Shraddha", "Moni", "Booni"]
print(random.choice(members))
