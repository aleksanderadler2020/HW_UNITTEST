import unittest
import pytest
from Task_1_1 import is_short_course, is_long_course
from Task_1_2 import check_dict
from Task_1_3 import link_course


# у меня в этих заданиях и функций то нет... пришлось изобретать хоть что нибудь
# но смысл юнит тестов понятен!
class TestCourse:

    @pytest.mark.parametrize('course, expected',
                             (
                                     ["Java-разработчик с нуля", False],
                                     ["Fullstack-разработчик на Python", False],
                                     ["Python-разработчик с нуля", True],
                                     ["Frontend-разработчик с нуля", False]
                             ))
    def test_short_course_equal(self, course, expected):
        assert is_short_course(course) == expected

    @pytest.mark.parametrize('course, expected',
                             (
                                     ["Java-разработчик с нуля", False],
                                     ["Fullstack-разработчик на Python", True],
                                     ["Python-разработчик с нуля", False],
                                     ["Frontend-разработчик с нуля", True]
                             ))
    def test_long_course_equal(self, course, expected):
        assert is_long_course(course) == expected

    @pytest.mark.parametrize('sort_dict, expected',
                             (
                                     [{12: [], 14: [], 20: []}, True],
                                     [{20: [], 14: [], 12: []}, False],
                                     [{14: [], 12: [], 20: []}, False]
                             ))
    def test_check_sort(self, sort_dict, expected):
        assert check_dict(sort_dict) == expected


class TestCourseUT(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(link_course([2, 0, 1, 3], [2, 0, 1, 3]), bool)

    def test_equal(self):
        self.assertEqual(link_course([2, 0, 1, 3], [2, 0, 1, 3]), True)
        self.assertEqual(link_course([2, 0, 1, 3], [2, 2, 1, 3]), False)

    def test_raise(self):
        with self.assertRaises(TypeError):
            link_course({}, [2, 2, 1, 3])
