

class toyota():
    def __init__(self):
        self.__engine = "goldenNuggetPower"
        self._steeringWheel = "standardSteel"

    def setEngine(self, changedEngine):
        self.__engine = "changedEngine"

    def getEngineName(self):
        print(self.__engine)

corolla = toyota()
corolla._steeringWheel = "goldFinish"
corolla.getEngineName()
corolla.setEngine("purplePowerPandito")
corolla.getEngineName()
