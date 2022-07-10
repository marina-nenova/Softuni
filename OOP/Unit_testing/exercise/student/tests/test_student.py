from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):

    def setUp(self) -> None:
        courses = {"Python": ["basic"]}
        self.student = Student("Test", courses)

    def test_student_init_if_not_courses(self):
        student = Student("Test")
        self.assertEqual("Test", student.name)
        self.assertEqual({}, student.courses)

    def test_student_if_courses_given(self):
        courses = {"Python": ["basic"]}
        student = Student("Test", courses)
        self.assertEqual("Test", student.name)
        self.assertEqual({"Python": ["basic"]}, student.courses)

    def test_student_enroll_if_given_course_name_in_courses(self):
        course_name = "Python"
        notes = ["advanced", "fundamentals"]
        add_course = "Y"
        result = self.student.enroll(course_name, notes, add_course)
        expected_notes = {"Python": ["basic", "advanced", "fundamentals"]}
        self.assertEqual(expected_notes, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_student_enroll_if_course_name_not_in_courses_and_add_notes_is_y(self):
        result = self.student.enroll("C#", ["a", "b"], "Y")
        expected_courses = {"Python": ["basic"], "C#": ["a", "b"]}
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_enroll_if_course_name_not_in_courses_and_add_notes_is_empty(self):
        result = self.student.enroll("C#", ["a", "b"], "")
        expected_courses = {"Python": ["basic"], "C#": ["a", "b"]}
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_enroll_if_course_name_not_in_courses_and_add_notes_not_valid(self):
        result = self.student.enroll("C#", ["a", "b"], "N")
        expected_courses = {"Python": ["basic"], "C#": []}
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_if_course_in_courses(self):
        result = self.student.add_notes("Python", "OOP")
        expected_courses = {"Python": ["basic", "OOP"]}
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("C#", ["a", "b"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_name_in_courses(self):
        result = self.student.leave_course("Python")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_if_course_name_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("C#")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
