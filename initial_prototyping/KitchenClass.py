# Initial prototype for creating meals class
# Paul Ambrose - 26/10/2022


class Kitchen():

    def __init__(self):
        self.Fridge = {"Milk": 50, "Bread": 400, "Banana": 20}
        self.Freezer = {}
        self.Cupboards = {}
        self.FruitBowl = {}
        self.VegSupply = {}

    def addItem(self, Item, Amount, Location):
      # if item to be added alredy in list, add amount to current item
      # Else, add new item and amount to list
