import unittest
from next_step import *

class NextStepTests(unittest.TestCase):
	def create_to_do_test(self):
		my_list = ToDo('To do list')
		self.assertEqual(my_list.name, 'To do list')
	
	def create_project_test(self):
		my_project = Project('Project')
		self.assertEqual(my_project.name, 'Project')
		
	def add_project_test(self):
		my_list = ToDo('David')
		my_list.add('Project')
		self.assertEqual(my_list.list_contents(), ['Project'])

	def access_project_test(self):
		m_list = ToDo('To Do List')
		m_list.add('Project')
		self.assertEqual(type(m_list[0]), Project)

	def create_tasks_test(self):
		my_project = Project('Work')
		my_project.add('Finish Deliverable')
		self.assertEqual(my_project.list_contents(), ['Finish Deliverable'])

	def add_project_to_list_test(self):
		my_list = ToDo('Overall List')
		my_list.add('Project')
		my_list[0].add('Task')
		self.assertEqual(my_list[0].list_contents(), ['Task'])

	def next_project_step_test(self):
		my_project = Project('Coding')
		my_project.add('Sign up for Thinkful')
		my_project.add('Complete Course')
		self.assertEqual(my_project.next_step(), 'Sign up for Thinkful')

	def all_next_steps_test(self):
		my_list = ToDo('Life')
		my_project = Project('Work')
		my_other_project = Project('Coding')
		my_list.add(my_project)
		my_list.add(my_other_project)
		my_list[0].add('Finish Deliverable')
		my_list[0].add('Finish Objectives')
		my_list[1].add('Complete Unit 2')
		my_list[1].add('Complete Unit 3')
		self.assertEqual(my_list.next_steps(), ['Finish Deliverable', 
												'Complete Unit 2'])

	def step_taken_test(self):
		my_project = Project('Work')
		my_project.add('First Step')
		my_project.add('Second Step')
		my_project.take_step()
		self.assertEqual(my_project.list_contents(), ['Second Step'])
		self.assertEqual(my_project.steps_taken, 1)

	def total_steps_taken_test(self):
		my_list = ToDo('Life')
		my_project = Project('Work')
		my_other_project = Project('Coding')
		my_list.add(my_project)
		my_list.add(my_other_project)
		my_list[0].add('Finish Deliverable')
		my_list[0].add('Finish Objectives')
		my_list[1].add('Complete Unit 2')
		my_list[1].add('Complete Unit 3')
		my_project.take_step()
		my_other_project.take_step()
		self.assertEqual(my_project.steps_taken, 1)
		self.assertEqual(my_list.total_steps_taken(), 2)

	def delete_projects_test(self):
		my_list = ToDo('Life')
		my_project = Project('Work')
		my_other_project = Project('Coding')
		another_project = Project('Class')
		my_list.add(my_project)
		my_list.add(my_other_project)
		my_list.add(another_project)
		my_list.delete(0)
		my_list.delete('Class')
		self.assertEqual(my_list.list_contents(), ['Coding'])