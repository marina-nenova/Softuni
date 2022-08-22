from project.core.validator.validator import Validator


class Client:
    receipt_id = 0

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        Validator.raise_if_phone_number_not_valid(value)
        self.__phone_number = value

    @staticmethod
    def get_next_receipt_id():
        Client.receipt_id += 1
        return Client.receipt_id
