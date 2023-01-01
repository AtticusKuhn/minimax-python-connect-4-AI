class Color:
    code='\x1b[91m'
    name="color"
    def __str__(self):
        return self.code + self.short + '\033[0m'
    def equals(self, other):
        return self.name == other.name
    def __eq__(self,other):
        return self.equals(other)
    def __hash__(self):
        return ord(self.short)
    def not_grey(self):
        return self.name != "Grey"
class Red(Color):
    code='\x1b[91m'
    name="Red"
    short="r"
class Blue(Color):
    code='\033[94m'
    name="Blue"
    short="b"
class Grey(Color):
    code='\033[90m'
    name="Grey"
    short="g"