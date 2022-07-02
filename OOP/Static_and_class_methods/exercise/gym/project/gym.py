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
        self.__add_entity(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_entity(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_entity(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_entity(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_entity(subscription, self.subscriptions)

    def __add_entity(self, entity, collection):
        if entity not in collection:
            collection.append(entity)

    @staticmethod
    def __get_instance_by_id(id, collection):
        return [x for x in collection if x.id == id][0]

    def subscription_info(self, subscription_id: int):
        subscription = Gym.__get_instance_by_id(subscription_id, self.subscriptions)
        customer = Gym.__get_instance_by_id(subscription.customer_id, self.customers)
        trainer = Gym.__get_instance_by_id(subscription.trainer_id, self.trainers)
        plan = Gym.__get_instance_by_id(subscription.exercise_id, self.plans)
        equipment = Gym.__get_instance_by_id(plan.equipment_id, self.equipment)

        info = [subscription, customer, trainer, equipment, plan]
        return "\n".join([repr(x) for x in info])
