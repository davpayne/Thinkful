import unittest, os, shutil
from pickler import list_pickler, unpickler

class PicklerTests(unittest.TestCase):
	def setUp(self):
		self.my_list = [1,2, 4, 'test']
		self.path = './pickles'
		os.makedirs(self.path)
		self.file = os.path.join(self.path, 'save.pkl')

	def test_compare_lists(self):
		list_pickler(self.my_list,self.file)
		another_list = unpickler(self.file)
		self.assertEqual(self.my_list, another_list)

	def tearDown(self):
		shutil.rmtree(self.path)