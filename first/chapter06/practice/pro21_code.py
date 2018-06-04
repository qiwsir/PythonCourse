#coding:utf-8
'''
21. 一个房子，不管是house还是apartment，都是由一个一个的房间（room）组成的。创建两个对象，一个是Room，通过每个房间的长宽得到房间面积；另一个是House，由若干个Room组成，并且各个Room的面积和为House的总面积，根据总面积，可以比较不同的House之间大小。
'''

from functools import total_ordering

class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.room_area = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space(self):
        return sum(r.room_area for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                self.living_space,
                self.style)

    def __eq__(self, other):
        return self.living_space == other.living_space

    def __lt__(self, other):
        return self.living_space < other.living_space

# Build a few houses, and add rooms to them
h1 = House('h1', 'Bieshu')
h1.add_room(Room('Master Bedroom', 100, 100))
h1.add_room(Room('Living Room', 80, 80))
h1.add_room(Room('Kitchen', 90, 90))

h2 = House('h2', 'Yiwo')
h2.add_room(Room('Master Bedroom', 1, 1))
h2.add_room(Room('Living Room', 2, 1))

h3 = House('h3', 'Woju')
h3.add_room(Room('Master Bedroom', 10, 10))
h3.add_room(Room('Living Room', 3, 3))
h3.add_room(Room('Kitchen', 1, 2))

houses = [h1, h2, h3]

print('Is h1 bigger than h2?', h1 > h2) # prints True
print('Is h2 smaller than h3?', h2 < h3) # prints True
print('Is h2 greater than or equal to h1?', h2 >= h1) # Prints False
print('Which one is biggest?', max(houses)) # Prints 'h3: 1101-square-foot Split'
print('Which is smallest?', min(houses)) # Prints 'h2: 846-square-foot Ranch'
