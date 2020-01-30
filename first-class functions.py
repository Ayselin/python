def redvelvet():
    print("This is just chocolate in disguise, you loser.")
def vanilla():
    print("Vanilla is the only way to go. Nothing vanilla about vanilla.")
def chocolate():
    print("Chocolate is just naked red velvet.")
def angelfood():
    print("So soft. So fluffy. So good.")
def carrot():
    print("Just eat regular cake, you weirdo.")
cake_dictionary = {
    1 : redvelvet,
    2 : vanilla,
    3 : chocolate,
    4 : angelfood,
    5 : carrot
}
while True:
    message = """
    Pick a number corresponding to your cake choice.
    1. Red Velvet
    2. Vanilla
    3. Chocolate
    4. Angel Food
    5. Carrot
    Or press 6 to quit.
    """
    cakeoptions = int(input(message))
    if cakeoptions in range(1,6):
        cake_dictionary[cakeoptions]()
    else:
        break