earth_metals = ["mercury", "copper", "silver", "gold", "magnesium"]
earth_metals.sort(reverse=False)
print(earth_metals)
# can't use sort for tuples
planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.040),
    ]
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)
## changes the list itself
## sort changes the list
##  prints from largest planet to smallest
density = lambda planet: planet[2]
planets.sort(key=density, reverse=True)
print(planets)
sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)

print(sorted("Alphabetical"))