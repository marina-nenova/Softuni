from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def test_mammal_name_is_initialized_correctly(self):
        dog = Mammal("Loki", "Dog", "Woof!")
        self.assertEqual("Loki", dog.name)

    def test_mammal_type_is_initialized_correctly(self):
        dog = Mammal("Loki", "Dog", "Woof!")
        self.assertEqual("Dog", dog.type)

    def test_mammal_sound_is_initialized_correctly(self):
        dog = Mammal("Loki", "Dog", "Woof!")
        self.assertEqual("Woof!", dog.sound)

    def test_mammal_kingdom_initialised_correctly(self):
        def test_mammal_sound_is_initialized_correctly(self):
            dog = Mammal("Loki", "Dog", "Woof!")
            self.assertEqual("animals!", dog._Mammal__kingdom)

    def test_mammal_make_sound_returns_string(self):
        dog = Mammal("Loki", "Dog", "Woof!")
        result = dog.make_sound()
        self.assertEqual("Loki makes Woof!", result)

    def test_get_kingdom(self):
        dog = Mammal("Loki", "Dog", "Woof!")
        self.assertEqual("animals", dog.get_kingdom())

    def test_info_method_returns_correct_string(self):
        dog = Mammal("Loki", "Dog", "Woof!")
        result = dog.info()
        self.assertEqual("Loki is of type Dog", result)


if __name__ == "__main__":
    main()