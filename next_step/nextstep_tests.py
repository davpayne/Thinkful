import unittest
from next_step import *

class NextStepTests(unittest.TestCase):
	def create_to_do_test(self):
		my_list = ToDo('David')
		self.assertEqual(my_list.name, 'David')
	
	def create_project_test(self):
		my_project = Project('Test')
		self.assertEqual(my_project.name, 'Test')
		
	def add_project_test(self):
		my_list = ToDo('David')
		my_list.add('Project')
		self.assertEqual(my_list.list_contents(), ['Project'])

	"""
	def display_tasks_test(self):
		my_list = to_do()
		my_list.add_project('Learning')
		my_list.add_task('Learning', 'Finish lesson 6')
		my_list.add_task('Learning', 'Finish lesson 6')
	"""