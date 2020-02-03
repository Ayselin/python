from random import randint

class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)

def roll(sides):    
    d = Die(sides)
    d.roll_die()

    results = []
    for _ in range(10):
        result = d.roll_die()
        results.append(result)
    return results
    # return [for _ in range(10): results.d.roll().append(result)]
print(roll(6))
print(roll(10))
print(roll(20))


    # d = Die(20)
    # d.roll_die()

    # results = []
    # for num in range(10):
    #     result = d.roll_die()
    #     results.append(result)
    # print(results)