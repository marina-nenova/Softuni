from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Loki", "Dog", "Woof!")

    def test_mammal_init(self):
        self.assertEqual("Loki", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("Woof!", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_mammal_make_sound_returns_string(self):
        result = self.mammal.make_sound()
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", result)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method_returns_correct_string(self):
        result = self.mammal.info()
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", result)


if __name__ == "__main__":
    main()