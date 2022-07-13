from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.src = StudentReportCard("Test", 5)

    def test_report_card_initialized_correctly_with_valid_data(self):
        src = StudentReportCard("Test", 5)
        self.assertEqual("Test", src.student_name)
        self.assertEqual(5, src.school_year)
        self.assertEqual({}, src.grades_by_subject)

    def test_student_name_set_up_with_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("", 5)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_set_up_with_value_less_than_one_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Test", 0)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_set_up_with_valid_number(self):
        for grade in range(1, 13):
            self.src.school_year = grade
            self.assertEqual(grade, self.src.school_year)

    def test_school_year_set_up_with_value_more_than_twelve_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Test", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_property_returns_correct_value(self):
        self.assertEqual(5, self.src.school_year)

    def test_add_grade_adds_subject_that_does_not_exist_to_grades_by_subject(self):
        self.src.add_grade("Math", 5)
        expected = {"Math": [5]}
        self.assertEqual(expected, self.src.grades_by_subject)

    def test_add_grade_adds_grade_to_subject_that_exists_to_grades_by_subject(self):
        self.src.add_grade("Math", 5)
        self.src.add_grade("Math", 6)
        expected = {"Math": [5, 6]}
        self.assertEqual(expected, self.src.grades_by_subject)

    def test_average_grade_by_subject_returns_correct_string(self):
        self.src.add_grade("Math", 5)
        self.src.add_grade("Math", 6)
        self.src.add_grade("Bio", 4)
        self.src.add_grade("Bio", 6)
        expected = "Math: 5.50\nBio: 5.00"
        self.assertEqual(expected, self.src.average_grade_by_subject())

    def test_average_grade_for_all_subjects_returns_correct_string(self):
        self.src.add_grade("Math", 5)
        self.src.add_grade("Math", 6)
        self.src.add_grade("Bio", 4)
        self.src.add_grade("Bio", 6)
        expected = "Average Grade: 5.25"
        self.assertEqual(expected, self.src.average_grade_for_all_subjects())

    def test_repr_returns_correct_string(self):
        self.src.add_grade("Math", 5)
        self.src.add_grade("Math", 6)
        self.src.add_grade("Bio", 4)
        self.src.add_grade("Bio", 6)

        expected = "Name: Test\nYear: 5\n----------\nMath: 5.50\nBio: 5.00\n----------\nAverage Grade: 5.25"

        self.assertEqual(expected, repr(self.src))


if __name__ == "__main__":
    main()
