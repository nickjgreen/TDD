from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\Python\Projects\TDD\superlists\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def add_item_to_table(self, input):
        inputbox =self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(input)
        inputbox.send_keys(Keys.ENTER)


    def test_userTest(self):
        self.browser.get('http://localhost:8000')

        # Confirm title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Confirm To-Do input box takes input
        self.add_item_to_table('Test Item 1')
        time.sleep(3)

        # Confirm Item added to table
        self.check_for_row_in_table('1: Test Item 1')

        # Add another Item
        


        # self.fail('Finish tests')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
