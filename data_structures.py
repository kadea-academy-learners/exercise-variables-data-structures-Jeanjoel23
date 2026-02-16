

def main():
    # 1) Inputs (respecte exactement les prompts)
    name = input("Entrer le Nom complet : ")
    city = input("Entrer la ville: ")
    birth_year = int(input("Entrer l'année de naissance: "))
    current_year = int(input("Entrer l'année actuelle: "))
    foods_raw = input("Entrer vos aliments préférés : ")

    # 2) Variables & structures de données
    age =  current_year - birth_year
    foods_list = [food.strip() for food in foods_raw.split(',')]
    foods_set = set(foods_list)

    profile_dict = {'name': name, 'city': city, 'age': age, 'foods': foods_list}

    summary_tuple = (name, age, city)

    # 3) Output (garde exactement ces libellés)
    print("--------------------")
    print(f"Name: {name}")
    print(f"City: {city}")
    print(f"Age: {age}")
    print(f"Foods (list): {foods_list}")
    print(f"Foods count: {len(foods_list)}")
    print(f"Unique foods: {len(foods_set)}")
    print(f"Profile (dict): {profile_dict}")
    print(f"Summary (tuple): {summary_tuple}")
    print("--------------------")

if __name__ == "__main__":
    main()
