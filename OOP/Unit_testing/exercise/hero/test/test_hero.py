from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Warrior", 10, 100, 50)
        self.enemy = Hero("Defender", 10, 100, 50)

    def test_hero_init(self):
        username = "Test"
        level = 10
        health = 100
        damage = 50
        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_battle_raises_when_hero_names_match(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_when_hero_health_is_zero_or_negative(self):
        for health in [0, -50]:
            self.hero.health = health
            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raises_when_enemy_health_is_zero_or_negative(self):
        for health in [0, -50]:
            self.enemy.health = health
            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_returns_draw_when_both_heroes_die(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_returns_player_wins_when_enemy_dies(self):
        self.enemy.damage = 1
        result = self.hero.battle(self.enemy)
        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_returns_player_loses_when_player_dies(self):
        self.hero.damage = 1
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(55, self.enemy.damage)
        self.assertEqual(95, self.enemy.health)
        self.assertEqual(-400, self.hero.health)

    def test_string_returns_correct_string(self):
        expected = f"Hero Warrior: 10 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 50\n"
        result = str(self.hero)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
