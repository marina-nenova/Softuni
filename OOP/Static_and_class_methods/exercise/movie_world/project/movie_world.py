class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __get_customer(self, customer_id):
        return [existing_customer for existing_customer in self.customers if existing_customer.id == customer_id][0]

    def __get_dvd(self, dvd_id):
        return [existing_dvd for existing_dvd in self.dvds if existing_dvd.id == dvd_id][0]

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return "\n".join([repr(x) for x in self.customers]) + "\n" + "\n".join([repr(x) for x in self.dvds])
