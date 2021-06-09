class Car:
    def __init__(self,color,made,model,registration):
        self.color=color
        self.model=model
        self.registration=registration
        self.made=made

    def drive(self):
        return f"hello my model is {self.model}, {self.made} and the {self.registration} and it is {self.color}"



    def hoot(self):
         hoot=("rrrrrrr")
         mileage=(34567)
         return f" the car {self.hoot} and {self.mileage}"