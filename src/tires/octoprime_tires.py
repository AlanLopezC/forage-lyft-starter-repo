
from src.tires.tires import Tires


class OctoprimeTires(Tires):

    def needs_service(self):
        if sum(self.tires_worned) >= 3:
            return True
        else:
            return False
