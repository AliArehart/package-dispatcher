class Package:
    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass
        self.bulky = self.is_bulky()
        self.heavy = self.is_heavy()
        self.validate()

    def validate(self):
        if not all(isinstance(x, int) for x in [self.width, self.height, self.length, self.mass]):
            raise ValueError("All dimensions must be integers")
        if not all(x > 0 for x in [self.width, self.height, self.length, self.mass]):
            raise ValueError("All dimensions must be positive")

    def is_bulky(self):
        if self.width * self.height * self.length > 10_000_000:
            return True
        if self.width > 150 or self.height > 150 or self.length > 150:
            return True
        return False

    def is_heavy(self):
        return self.mass > 20

    def get_bulky(self):
        return self.bulky

    def get_heavy(self):
        return self.heavy


def dispatcher(package):
    bulky = package.get_bulky()
    heavy = package.get_heavy()

    if not bulky and not heavy:
        return "Standard"
    elif (bulky and not heavy) or (not bulky and heavy):
        return "Special"
    return "Rejected"


def sort_package(width, height, length, mass):
    package = Package(width, height, length, mass)
    return dispatcher(package)
