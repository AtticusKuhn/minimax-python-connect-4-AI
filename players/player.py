class Player:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def get_move(self, boardstate):
        raise Exception("not implemented")
    def is_my_color(self,  color):
        return color.equals(self.color)
    def is_enemy_color(self, color):
        return (not self.is_my_color(color)) and  color.not_grey()
    def __str__(self):
        return str(self.color)