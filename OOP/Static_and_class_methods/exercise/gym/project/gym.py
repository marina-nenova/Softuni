from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def __get_instance(id, collection):
        return [x for x in collection if x.id == id][0]

    def subscription_info(self, subscription_id: int):
        subscription = Gym.__get_instance(subscription_id, self.subscriptions)
        customer = Gym.__get_instance(subscription.customer_id, self.customers)
        trainer = Gym.__get_instance(subscription.trainer_id, self.trainers)
        plan = Gym.__get_instance(subscription.exercise_id, self.plans)
        equipment = Gym.__get_instance(plan.equipment_id, self.equipment)

        info = [subscription, customer, trainer, equipment, plan]
        return "\n".join([repr(x) for x in info])
