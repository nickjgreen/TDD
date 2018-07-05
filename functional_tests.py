from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\Python\Projects\TDD\superlists\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_userTest(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        # self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
