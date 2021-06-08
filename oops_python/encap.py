class Car:
    def __init__(self):
        self.type = 'sport'  # public
        self._automatic = False  # Protected
        self.__maxspeed = 200   # Private


    # public method
    def drive(self):
        print("driving")

    # protected
    def _accelerate(self):
        print("accelerating")

    # private
    def __update_software(self):
        print("updating software")



c = Car()
c.drive()
c._accelerate()
# c.__update_software() # it will give error
c._Car__update_software()
# print(c.__maxspeed)
