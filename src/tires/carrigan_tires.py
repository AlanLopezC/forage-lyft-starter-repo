
from src.tires.tires import Tires


class CarriganTires(Tires):

    def needs_service(self):
        if any(num >= 0.9 for num in self.tires_worned):
            return True
        else:
            return False
