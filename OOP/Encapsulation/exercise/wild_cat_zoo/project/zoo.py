from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:

            if self.__budget < price:
                return "Not enough budget"

            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for existing_worker in self.workers:
            if existing_worker.name == worker_name:
                self.workers.remove(existing_worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        care_expenses = sum([animal.money_for_care for animal in self.animals])

        if self.__budget >= care_expenses:
            self.__budget -= care_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_dict = {"Lions": [], "Tigers": [], "Cheetahs": []}

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                animals_dict["Lions"].append(animal)
            elif animal.__class__.__name__ == "Tiger":
                animals_dict["Tigers"].append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                animals_dict["Cheetahs"].append(animal)

        output = f"You have {len(self.animals)} animals\n"

        for animal_type, animals in animals_dict.items():
            output += f"----- {len(animals)} {animal_type}:\n"
            for animal in animals:
                output += repr(animal) + "\n"

        return output.strip()


    def workers_status(self):
        workers_dict = {"Keepers": [], "Caretakers": [], "Vets": []}

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                workers_dict["Keepers"].append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                workers_dict["Caretakers"].append(worker)
            elif worker.__class__.__name__ == "Vet":
                workers_dict["Vets"].append(worker)

        output = f"You have {len(self.workers)} workers\n"

        for worker_type, workers in workers_dict.items():
            output += f"----- {len(workers)} {worker_type}:\n"
            for worker in workers:
                output += repr(worker) + "\n"

        return output.strip()