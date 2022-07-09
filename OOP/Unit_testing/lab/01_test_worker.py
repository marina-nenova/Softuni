class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_initialized_correctly(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)

    def test_worker_energy_decreased_after_working(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        worker.work()
        self.assertEqual(9, worker.energy)
        worker.work()
        self.assertEqual(8, worker.energy)

    def test_worker_tries_to_work_with_zero_energy(self):
        worker = Worker("Test", 100, 0)
        self.assertEqual(0, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_tries_to_work_with_negative_energy(self):
        worker = Worker("Test", 100, -1)
        self.assertEqual(-1, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_increased_after_working(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(0, worker.money)

        worker.work()
        self.assertEqual(worker.money, 100)

        worker.work()
        self.assertEqual(worker.money, 200)

    def test_worker_energy_increased_after_resting(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)
        worker.rest()
        self.assertEqual(12, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 100, 10)
        result = worker.get_info()
        self.assertEqual('Test has saved 0 money.', result)


if __name__ == "__main__":
    main()
