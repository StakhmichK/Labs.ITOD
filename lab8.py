A = [1, 2, 3, 4, 5]
for element in A:
    print(element)

x = 11
y = 1
while y < x:
    print(y)
    y += 1

for i in range(-5, 6):
    print(i)

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for color in squares:
    print(color)

bands = ['Metallica', 'Metallica', 'Nirvana', 'Queen', 'Metallica']
favorite_bands = []
i = 0
while i < len(bands) and bands[i] == 'Metallica':
    favorite_bands.append(bands[i])
    i += 1
print(favorite_bands)

def f(a, b):
    return a * b
a = 4
b = 2
if a * b == f(a, b):
    print("correct")
else:
    print("incorrect")

class Star:
    def __init__(self, name, constellation, star_type):
        self.name = name
        self.constellation = constellation
        self.star_type = star_type
        self.discovery_count = 0

    def star_info(self):
        print("Star name:", self.name)
        print("Constellation:", self.constellation)
        print("Star type:", self.star_type)
        print("Times observed:", self.discovery_count)

    def observe(self):
        self.discovery_count += 1

my_star = Star("Sirius", "Canis Major", "Main Sequence")

my_star.star_info()

for i in range(5):
    my_star.observe()
my_star.star_info()