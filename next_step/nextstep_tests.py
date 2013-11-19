import unittest
from next_step import *

class NextStepTests(unittest.TestCase):
	def create_to_do_test(self):
		my_list = to_do('David')
		self.assertEqual(my_list.name, 'David')
		"""
	def add_project_test(self):
		my_list = to_do('David')
		my_list.add_project('Test')
		self.assertEqual(my_list.projects, ['Test'])
	
	def display_tasks_test(self):
		my_list = to_do()
		my_list.add_project('Learning')
		my_list.add_task('Learning', 'Finish lesson 6')
		my_list.add_task('Learning', 'Finish lesson 6')
	"""