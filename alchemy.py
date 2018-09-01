import csv

# START database creation
def create_reagents_db():
    '''
    Creates a dictionary from csv file to associate each reagent with its corresponding potion effects
    :return Dictionary {reagent: [effects]}
    '''
    raw = []
    f = open('Ingredients.csv', newline='')
    for row in f:
        raw.append([x.strip().lower() for x in row.rstrip().split(',')])
    db = {row[0]: [row[1], row[2],row[3], row[4]] for row in raw}
    f.close()
    return db

def create_effects_db():
    '''
    Creates a dictionary from csv file to associate each effect with its corresponding reagents
    :return Dictionary {effect: [reagents]}
    '''
    raw = []
    f = open('Effects.csv', newline='')
    for row in f:
        raw.append([x.strip().lower() for x in row.rstrip().split(',')])
    f.close()
    effects = {x[1] for x in raw}
    db = {e: [] for e in effects}
    for row in raw:
        db[row[1]].append(row[0])
    return db
# END database creation
def print_potion(reagents, effects):
    print('Current Potion')
    print(reagents)
    print(effects)
    print()

def get_input(reagents_db):
    while True:
        reagent = input('Enter a reagent or type a letter to filter list: ')
        reagent = reagent.lower()
        if reagent in reagents_db.keys():
            return reagent
        elif len(reagent) == 1:
            for r in reagents_db:
                if r[0] == reagent:
                    print(r)
        elif reagent == 'exit' or reagent == 'quit':
            return 'exit'
        else:
            print('Invalid entry: {}'.format(reagent))

def create_pot(reagents_db, effects_db):
    '''
    Creates a new potion from reagents.
    '''
    reagents = []
    effects = []
    # Add first reagent
    first = get_input(reagents_db)
    if first == 'exit':
        return
    reagents.append(first)
    # adding second reagent
    # options shown by effect
    print()
    for eff in reagents_db[reagents[0]]:
        print(eff)
        print('--------------------------------------------')
        for rea in effects_db[eff]:
            if rea not in reagents:
                print(rea)
        print()
    second = get_input(reagents_db)
    while second in reagents:
        print('Please choose a unqiue reagent')
        print('Current reagents added: ', end='')
        print(reagents)
        second = get_input(reagents_db)
    if second == 'exit':
        return
    reagents.append(second)
    # add effects
    effects += list(set(reagents_db[reagents[0]]) & set(reagents_db[reagents[1]]))
    print_potion(reagents, effects)
    if input('Add third ingredient [Y/n]: ') == 'n':
        return
    for r in reagents:
        for eff in reagents_db[r]:
            if eff in effects:
                continue
            print(eff)
            print('--------------------------------------------')
            for rea in effects_db[eff]:
                if rea not in reagents:
                    print(rea)
            print()
    third = get_input(reagents_db)
    while third in reagents:
        print('Please choose a unqiue reagent')
        print('Current reagents added: ', end='')
        print(reagents)
        third = get_input(reagents_db)
    if third == 'exit':
        return
    reagents.append(third)
    effects += list(set(reagents_db[reagents[0]]) & set(reagents_db[reagents[2]]))
    effects += list(set(reagents_db[reagents[1]]) & set(reagents_db[reagents[2]]))
    effects = list(set(effects))
    print_potion(reagents, effects)
    print()
    input('Press any key to continue')

def search_effect(reagents_db, effects_db):
    while True:
        eff = input("Enter an effect or 'list' to see all available effects: ")
        if eff.lower() == 'list':
            i = 0
            for e in effects_db:
                print(str(i) + ": " + e)
                i += 1
        elif eff in effects_db.keys():
            for e in effects_db[eff]:
                print(e)
            print()
            if input("Search another effect? [Y/n]: ") == 'n':
                return
        elif eff == 'exit' or eff == 'quit':
            return
        else:
            print('Invalid Input')

def main():
    reagents = create_reagents_db()
    effects = create_effects_db()
    menu_options = ["Make Potion by Ingredient", "Search by effect", "Quit"]
    print("Welcome to the Skyrim Alchemy helper")
    while(True):
        for i in range(1, 4):
            print(str(i) + ": " + menu_options[i-1])
        choice = int(input("Enter your selection: "))
        if choice == 1:
            create_pot(reagents, effects)
        elif choice == 2:
            search_effect(reagents, effects)
        elif choice == 3:
            break
        elif choice == 4:
            for r in reagents:
                print(r + ":", end=' ')
                print(reagents[r])
        elif choice == 5:
            for e in effects:
                print(e + ":", end=' ')
                print(effects[e])
        else:
            print("Invalid Input")

if __name__ == '__main__':
    main()
