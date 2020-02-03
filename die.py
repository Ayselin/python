from random import randint

class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)

    # append 1 side randomly, 10 times


def roll(sides):    
    die = Die(sides) # initializes Die with a number of sides
    # results = [] # empty list to store
    # # print a range of numbers from the numbers that are stored inside the function roll
    # for _ in range(10):
    #     # result = die.roll_die()
    #     results.append( die.roll_die() )
    # return results

    return [ die.roll_die() for _ in range(10) ]

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