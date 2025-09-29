import  sys
cookbook = {
        "sandwich" : {
            "ingredients": ["ham", "bread", "cheese", "tomatoes"],
            "meal" :"lunch",
            "prep_time" : 10
        },
        "cake" : {
            "ingredients": ["flour", "sugar", "eggs"],
            "meal" :"dessert",
            "prep_time" :60
        },
        "salad" : {
            "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
            "meal" :"lunch",
            "prep_time" : 15
        }
}

def print_recipes_name():
    for recipe in cookbook:
        print(recipe)

def print_details(recipe):
    r = cookbook.get(recipe)
    if r is None:
        print("recipe not found")
        return
    print("Recipe for "+ recipe + ":")
    print("\tIngredients list:", r["ingredients"]) 
    print("\tTo be eaten for " + r["meal"] + ".") 
    print(f"\tTakes {r['prep_time']} minutes of cooking.")
def delete_recipe(recipe):
    if cookbook.pop(recipe, None) is None:
        print(f"Recipe not found...Can't delete {recipe}")

def add_recipe():
    name = input (">>> Enter a name:\n")
    ingr_list = []
    ingr = input (">>> Enter ingredients:\n")
    while (ingr != ""):
        ingr_list.append(ingr)
        ingr = input("")
    meal = input (">>> Enter a meal type:\n")
    try:
        time = int(input (">>> Enter a preparation time:\n"))
    except ValueError:
        print("Invalid time")
        return
    cookbook[name] = {
            "ingredients": ingr_list,
            "meal": meal,
            "prep_time": time
    }

print("Welcome to the Python Cookbook !")
while(True):
    print("""List of available options:
        1: Add a recipe
        2: Delete a recipe
        3: Print a recipe
        4: Print the cookbook
        5: Quit\n""")
    command = input("Please select an option:\n>> ").strip()
    match command:
        case "1":
            add_recipe()
        case "2":
            answer = input("\nPlease enter a recipe name to delete:\n")
            delete_recipe(answer)
        case "3":
            answer = input("\nPlease enter a recipe name to get its details:\n")
            print_details(answer)
        case "4":
            print_recipes_name()
        case "5":
            print("\nCookbook closed. Goodbye !")
            break
        case _:
            print("\nSorry, this option does not exist.")

