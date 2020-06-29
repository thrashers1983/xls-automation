# 我理解测试的目的，是写一个自动化脚本来执行针对函数或者类的不同方面的各个角度的测试，这样每次修改函数或者类的时候，就执行一次测试脚本就能知道改动
# 有没有破坏其原来的功能，否则的话，每次改动后都要手动测试是非常浪费时间的
# 一个unit test用来确保一个函数的一个特定方面是工作正常的，一个test case是一系列unit test的集合，来保证函数整体工作正常，测试类也一样，一个
# unit test测试类的一个方法，一个test case测试整个类

import unittest
from chapter11_functions_classes import get_formatted_name
from chapter11_functions_classes import AnonymousSurvey


# 测试函数
class NamesTestCase(unittest.TestCase):             # 类名最好有待测试的函数名和Test
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):                 # 测试方法必须以test_开头，当运行当前脚本的时候，以test_开头的方法名会被自动执行
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# 测试类
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


# 上面这个测试类要在每个测试方法里都创建一个被测类的实例，有很多重复劳动，可以用setUp()方法一次性创建这些被测类的实例和属性，这些实例和属性在每一
# 个测试方法里都可以被使用，python会先运行setUp()方法，再运行test_开头的方法
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
