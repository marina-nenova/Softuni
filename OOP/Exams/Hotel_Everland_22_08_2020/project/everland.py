from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                output.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(output)

    def status(self):
        total_population = sum([room.members_count for room in self.rooms])
        output = f"Total population: {total_population}\n"
        for room in self.rooms:
            output += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            child_count = 1
            for child in room.children:
                output += f"--- Child {child_count} monthly cost: {child.get_monthly_expense():.2f}$\n"
                child_count += 1
            if hasattr(room, "appliances"):
                output += f"--- Appliances monthly cost: {sum([app.get_monthly_expense() for app in room.appliances]):.2f}$\n"
        return output.strip()
