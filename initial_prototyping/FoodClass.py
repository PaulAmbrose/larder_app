# Initial prototype for food class
# Paul Ambrose - 25/10/2022


class food():

    def __init__(self, FoodType, FoodStoreLoc, FoodCost, FoodAmount, FoodMacroNut):
        self.FoodType
        self.FoodStoreLoc
        self.FoodCost  # per 100g
        self.FoodAmount  # in grams
        self.FoodMacroNut  # CarbsProtenFat tuple for % of each e.g (10,10,80)

        self.FoodType = FoodType,
        self.FoodStoreLoc = FoodStoreLoc,
        self.FoodCost = FoodCost,
        self.FoodAmount = FoodAmount,
        self.FoodMacroNut = FoodMacroNut

    def FoodMoneyValue(self):
        FoodMoneyValue = (self.FoodAmount/100) * self.FoodCost
        return FoodMoneyValue
