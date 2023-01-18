"""
Les listes peuvent être constituer de différentes manières
Voici un ensemble de liste en Python
"""
a = [1, 3, 4, 2]
b = [[1, 2 ,3], [4, 5, 7]]
c = [1 + 2, "a" * 5, 3]

print("____", a, "____", b, "____", c)


"""
Créer une liste
"""
zones = ["Abidjan", "Grand-Lahou", "Grand-Béréby", "Yamoussoukro", "Sassandra", "Fresco"]

trois_premiers_elements = zones[:3]
trois_derniers_elements = zones[3:]
print("____", trois_premiers_elements, "_____", trois_derniers_elements)
print("____", zones[1][-1], "____")


"""
Manipulation des listes
"""
manupilation_des_listes = ["a", "b", "c", "d"]
manupilation_des_listes[1] = "z"
manupilation_des_listes[2:] = ["s", "t"]

print("____", manupilation_des_listes, "_____")


