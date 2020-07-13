

from abc import ABC, abstractmethod

class building(ABC):
    def height(self):
        pass

class skyscraper(building):
    def height(self):
        print("I am over 150ft tall!")

bigPink = skyscraper()
bigPink.height()
