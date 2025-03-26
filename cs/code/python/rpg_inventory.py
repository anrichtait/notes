def displayInventory(inventory):
    itemTotal = 0
    print("Inventory:")

    for item, amount in inventory.items():
        print(f"{item}: {amount}")
        itemTotal += amount


def add_item(items, inventory):
    for item in items:
        for currentItem, amount in inventory.items():
            if currentItem == item:
                inventory[item] += 1
    displayInventory(inventory)


def menu(lotteryLoot, dragonLoot, inventory):
    print("You are travelling down a dark road at night and something stinks!\n")
    print("You notice the smell getting stronger and consider following it off the side of the path into the woods. Which way will you go?")
    print("Options:")
    print("- Left")
    print("- Right")
    print("- Straight")
    print(">> ")
    userInput = input().strip().lower()
    if userInput == 'left':
        print("You got lost and starved to death.")
    elif userInput == 'right':
        print("You found a large dead dragon with a leather bag clutched in it's talon!")
        print(f"Prying the bag from the dragon's cold dead claws you find {dragonLoot}!")
        add_item(dragonLoot, inventory)
    elif userInput == 'straight':
        print("You went on home and ended up living a very normal, boring life.")
        print("You won the lottery at age 99, one day before you died.")
        add_item(lotteryLoot, inventory)
    else:
        print("Input error, please make sure you give one of the options!")
        menu()


def main():
    inventory = {
            'rope': 1,
            'torch': 6,
            'gold coin': 42,
            'dagger': 1,
            'arrow': 12
            }
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    lotteryLoot = ['gold coin'] * 1000000
    menu(lotteryLoot, dragonLoot, inventory)


main()
