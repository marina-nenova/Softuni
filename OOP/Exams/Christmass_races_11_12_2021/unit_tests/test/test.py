from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("Test")
        self.team2 = Team("TestTwo")

    def test_team_initialized_correctly_with_valid_data(self):
        name = "Test"
        team = Team(name)
        self.assertEqual(name, team.name)
        self.assertEqual({}, team.members)

    def test_raise_if_name_not_alpha(self):
        with self.assertRaises(ValueError) as ex:
            Team("Test1")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_team_add_member_adds_correctly_if_name_not_in_members_dict(self):
        self.team.add_member(ana=20, eva=21)
        self.assertEqual({"ana": 20, "eva": 21}, self.team.members)
        self.team.add_member(ana=20)
        self.assertEqual({"ana": 20, "eva": 21}, self.team.members)

    def test_team_add_member_returns_correct_string(self):
        result = self.team.add_member(ana=20, eva=21)
        self.assertEqual({"ana": 20, "eva": 21}, self.team.members)
        expected = "Successfully added: ana, eva"
        self.assertEqual(expected, result)

    def test_remove_member_removes_if_member_in_members(self):
        self.team.add_member(ana=20, eva=21)
        result = self.team.remove_member("eva")
        self.assertEqual({"ana": 20}, self.team.members)
        self.assertEqual(f"Member eva removed", result)

    def test_remove_member_if_member_not_in_members_returns_correct_string(self):
        self.team.add_member(ana=20)
        result = self.team.remove_member("eva")
        self.assertEqual(f"Member with name eva does not exist", result)

    def test_greater_than_method_returns_correctly(self):
        self.team.add_member(ana=20, eva=21)
        self.team2.add_member(peter=23)
        result = self.team > self.team2
        self.assertEqual(True, result)

        result = self.team < self.team2
        self.assertEqual(False, result)

        self.team2.add_member(george=25)
        result = self.team > self.team2
        self.assertEqual(False, result)

    def test_len_method_returns_correctly(self):
        self.team.add_member(ana=20, eva=21)
        result = len(self.team)
        self.assertEqual(2, result)

    def test_add_method_creates_new_instance_from_two_teams(self):
        self.team.add_member(ana=20, eva=21)
        self.team2.add_member(peter=23)
        new_team = self.team + self.team2
        self.assertEqual("TestTestTwo", new_team.name)
        self.assertEqual({"ana": 20, "eva": 21, "peter": 23}, new_team.members)

    def test_str_method_returns_correct_string(self):
        self.team.add_member(ana=20, eva=21, alice=21)
        result = str(self.team)
        expected = "Team name: Test\n" \
                   "Member: alice - 21-years old\n" \
                   "Member: eva - 21-years old\n" \
                   "Member: ana - 20-years old"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
