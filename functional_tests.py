from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\Python\Projects\TDD\superlists\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_userTest(self):
        self.browser.get('http://localhost:8000')

        # Confirm title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Confirm To-Do input box takes input
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item')
        inputbox.send_keys('Test Item 1')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Confirm Item added to table
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Test Item 1' for row in rows), "New to-do item did not appear in table"
        )

        # Add another Item
        self.fail('Finish tests')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
