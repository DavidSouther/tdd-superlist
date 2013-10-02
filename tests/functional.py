from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list(self):
		# Edith has heard about a cool new online to-do app.
		# She goes to check out its home page.
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists.
		self.assertIn('To-do', self.browser.title)

		# She is invited to enter a todo item straight away

		# She types "Buy Peacock Feathers" into a text box
		# (Edith's hobby is tying fly-fishing lures).

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy Peacock Feathers" as an item in a to-do list.

		self.fail("Finish the feature!")

if __name__ == '__main__':
	unittest.main()

