class cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color 

    def set_color(self, color):
        self.color = color   

cookie_one = cookie('green')
cookie_two = cookie('blue')
cookie_one.set_color("red")
print(cookie_one.get_color())