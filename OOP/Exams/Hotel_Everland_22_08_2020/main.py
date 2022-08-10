from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child
from project.everland import Everland


everland = Everland()

young_couple = YoungCouple("Johnsons", 150, 205)

child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
alone_old = AloneOld("Peters", 300)
alone_young = AloneYoung("Adams", 500)
old_couple = OldCouple("Scott", 350, 320)
everland.add_room(young_couple)
everland.add_room(young_couple_with_children)
everland.add_room(alone_old)
everland.add_room(alone_young)
everland.add_room(old_couple)
print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())

# Output
#
# Monthly consumption: 1420.00$.
# Johnsons paid 242.00$ and have 113.00$ left.
# Peterson paid 894.00$ and have 226.00$ left.
# Peters paid 10.00$ and have 290.00$ left.
# Adams paid 55.00$ and have 445.00$ left.
# Scott paid 219.00$ and have 451.00$ left.
# Total population: 10
# Johnsons with 2 members. Budget: 113.00$, Expenses: 222.00$
# --- Appliances monthly cost: 222.00$
# Peterson with 4 members. Budget: 226.00$, Expenses: 864.00$
# --- Child 1 monthly cost: 270.00$
# --- Child 2 monthly cost: 150.00$
# --- Appliances monthly cost: 444.00$
# Peters with 1 members. Budget: 290.00$, Expenses: 0.00$
# Adams with 1 members. Budget: 445.00$, Expenses: 45.00$
# --- Appliances monthly cost: 45.00$
# Scott with 2 members. Budget: 451.00$, Expenses: 204.00$
# --- Appliances monthly cost: 204.00$




