from constraint import Problem, AllDifferentConstraint

# Définition des jours de la semaine et des créneaux horaires
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
slots = ["Slot1", "Slot2", "Slot3", "Slot4", "Slot5"]

# Définition des cours et des enseignants
courses = {
    "Math": ["John"],
    "Science": ["Alice"],
    "Literature": ["Bob"]
}

# Création d'une instance du problème
problem = Problem()

# Ajout des variables au problème (cours)
for day in days:
    for slot in slots:
        for course, teachers in courses.items():
            problem.addVariable((day, slot, course), teachers)

# Contraintes de base
# 2. Chaque jour doit avoir cinq créneaux horaires
# for day in days:
#     if day == "Tuesday":
#         problem.addConstraint(AllDifferentConstraint(), [(day, slot, course) for slot in slots[:3] for course in courses.keys()])
#     else:
#         problem.addConstraint(AllDifferentConstraint(), [(day, slot, course) for slot in slots for course in courses.keys()])

# 3. Pas plus de trois créneaux horaires successifs
# for day in days:
#     for i in range(len(slots) - 3):
#         problem.addConstraint(AllDifferentConstraint(), [(day, slot, course) for slot in slots[i:i+4] for course in courses.keys()])

# 4. Pas de cours identiques dans le même créneau horaire
for slot in slots:
    for day in days:
        problem.addConstraint(AllDifferentConstraint(), [(day, slot, course) for course in courses.keys()])

# 5. Différents cours pour le même groupe doivent avoir des allocations de créneaux différents

# Résolution du problème
solution = problem.getSolution()

# Affichage de la solution
if solution is not None:
    print("Tableau d'emploi du temps :\n")
    print("| Jour      | Heure  | Cours     | Enseignant |")
    print("---------------------------------------------")
    for day, slot, course in sorted(solution.keys()):
        teacher = solution[(day, slot, course)]
        print(f"| {day:<9} | {slot:<6} | {course:<15} | {teacher:<18} |")
else:
    print("Aucune solution trouvée.")
