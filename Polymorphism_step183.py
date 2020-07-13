

class humanoid():
    arms = 2
    legs = 2
    iq = 120

    def smashHead():
        iq = iq - 10


class human(humanoid):
    arms = 3
    legs = 2
    iq = 120


class romulan(humanoid):
    arms = 2
    legs = 2
    iq = 105

print(romulan.iq)
    
