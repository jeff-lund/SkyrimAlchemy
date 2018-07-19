import csv

# initializes db from csv
def create_db():
    raw = []
    f = open('si.csv', newline='')
    for row in f:
        raw.append([x for x in row.rstrip().split(',')])
    db = {row[0].strip(): [row[1].strip(), row[2].strip(),row[3].strip(), row[4].strip()] for row in raw}
    return db

def choose_first(db, ingredients):
    choice = input("Enter an ingredient, Choose filter letter, or 'exit' to exit: ")
    if choice == 'exit':
        return (9, [])
    elif not choice.replace(' ', '').isalpha():
        return (0, ingredients)
    elif len(choice) > 1:
        if choice in db:
            ingredients.append(choice)
        else:
            return (9, [])
    else:
        first = [entry for entry in db.keys() if entry[0] == choice.upper()]
        if len(first) == 0:
            print("-----------------------------------------------")
            print("No entries for that letter")
            print("-----------------------------------------------")
            return (9, [])
        for i in range(len(first)):
            print(str(i) + ":" + first[i])
        choice = input("Select an ingredient by number: ")
        if not choice.isdigit():
            print("-----------------------------------------------")
            print("Invalid choice")
            print("-----------------------------------------------")
            return (0, ingredients)
        elif int(choice) >= len(first):
            return (0, ingredients)
        ingredients.append(first[int(choice)])

    return (1, ingredients)

def choose_second(db, ingredients):
    index = 0
    effects = db[ingredients[0]]
    compat_ingredients = {}
    for e in effects:
        compat_ingredients[e] = []
        for entry in db:
            if entry not in ingredients and e in db[entry]:
                compat_ingredients[e].append(entry)
    for entry in effects:
        print("-----------------------------------------------")
        print(entry)
        print("-----------------------------------------------")
        for c in compat_ingredients[entry]:
            print(c)
    choice = input("Choose a second ingredient or q to quit: ")
    civ = (x for y in compat_ingredients.values() for x in y)
    if choice == 'q':
        return (9, [])
    elif choice not in civ:
        print("-----------------------------------------------")
        print('not in compatible ingredients')
        print("-----------------------------------------------")
        return (9, [])
    else:
        ingredients.append(choice)
        return (2, ingredients)

def choose_third(db, ingredients):
    choice = input("Press anything to add a third ingredient or 'exit' to print current potion")
    if choice == 'exit':
        return (3, ingredients)

    effects = []
    for x in ingredients:
        for y in db[x]:
            effects.append(y)
    compat_ingredients = {}
    for e in set(effects):
        compat_ingredients[e] = []
        for entry in db:
            if entry not in ingredients and e in db[entry]:
                compat_ingredients[e].append(entry)
    for entry in set(effects):
        print("-----------------------------------------------")
        print(entry)
        print("-----------------------------------------------")
        for c in compat_ingredients[entry]:
            print(c)
    current_effects = {x for x in effects if effects.count(x) > 1}
    print("Current Effects:")
    print(current_effects)
    choice = input("Choose a third ingredient or 'q' to quit: ")
    civ = (x for y in compat_ingredients.values() for x in y)
    if choice == 'q':
        return (9, [])
    elif choice not in civ:
        print("-----------------------------------------------")
        print('not in compatible ingredients')
        print("-----------------------------------------------")
        return (9, [])
    else:
        ingredients.append(choice)
    return (3, ingredients)


def create_pot(db):
    while(True):
        ingredients = []
        cont = 0
        while cont == 0:
            ret = choose_first(db, ingredients)
            cont = ret[0]
            ingredients = ret[1]
        while cont == 1:
            ret = choose_second(db, ingredients)
            cont = ret[0]
            ingredients = ret[1]
        while cont == 2:
            ret = choose_third(db, ingredients)
            cont = ret[0]
            ingredients = ret[1]
        effects = []
        potion = set()

        if cont == 9:
            return

        for i in ingredients:
            for x in db[i]:
                effects.append(x)
        for e in effects:
            if effects.count(e) > 1:
                potion.add(e)
        print("-----------------------------------------------")
        print("Ingredients: " + " | ".join(ingredients))
        print("-----------------------------------------------")
        print("Effects: " + " | ".join(potion))
        print("-----------------------------------------------")
        letter = input("Press anything for another potion or 'exit' to exit to the menu: ")
        if letter == 'exit':
            break

def search(db):
    pass

def main():
    db = create_db()
    menu_options = ["Make Potion by Ingredient", "Search by effect", "Quit"]
    print("Welcome to the Skyrim Alchemy helper")
    while(True):
        for i in range(1, 4):
            print(str(i) + ": " + menu_options[i-1])
        choice = int(input("Enter your selection: "))
        if choice == 1:
            create_pot(db)
        elif choice == 2:
            search(db)
        elif choice == 3:
            break
        else:
            print("Invalid Input")





if __name__ == '__main__':
    main()
