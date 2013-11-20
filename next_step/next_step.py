class ToDo(object): 
	contents = []
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		values = {'name':self.name}
		if len(self.contents) > 0:
			values['contents'] = [str(item.name) for item in self.contents]
		return str(values)

	def list_contents(self):
		if len(self.contents) > 0:
			list_contents = [str(item.name) for item in self.contents]
		return list_contents

	def add(self, pname):
		self.contents.append(Project(pname))

class Project(ToDo):
	def __repr__(self):
		return self.name
"""
if __name__ == '__main__':
    t = ToDo('test1')
    p = Project('Project1')
    t.add(p)
    print t
    print t.list_contents()"""