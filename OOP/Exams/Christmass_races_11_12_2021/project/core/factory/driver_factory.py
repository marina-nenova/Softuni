from project.driver import Driver


class DriverFactory:

    @staticmethod
    def create_driver(name):
        return Driver(name)
