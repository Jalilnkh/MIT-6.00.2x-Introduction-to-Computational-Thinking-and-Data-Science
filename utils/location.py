class Location():
    def __init__(self, x, y) -> None:
        """x and y are floats"""
        self.x = x
        self.y = y
    
    def move(self, delta_x, delta_y):
        """delta_x and delta_y are floats"""
        return Location(self.x + delta_x,
            self.y + delta_y)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def dist_from(self, other):
        x_dist = self.x - other.get_x()
        y_dist = self.y - other.get_y()
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self) -> str:
        return f'<{str(self.x)} , {str(self.y)} >'