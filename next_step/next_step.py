"""
next_step is a task manager intended to help the user focus on 
their next step only. It also tracks steps taken as a motivational tool.

'You don't have to see the whole staircase, just take the first step'
- Martin Luther King Jr.
"""

class Task(object):
    """
    Base class for task manager. Has only basic attributes Used as base
    for overall to do list and projects and is used as the task class.
    """
    def __init__(self, name):
        """
        Initializes the name of the object as well as the contents and
        steps taken, only used by ToDo and Project functions. Contents
        are the contained projects/tasks and steps taken tracks the progress
        of each project and overall. 
        """
        self.name = name
        self.contents = []
        self.steps_taken = 0

    def __repr__(self):
        """
        Returns the name of the object as well as the projects/tasks it contains
        """
        values = {'name':self.name}
        if len(self.contents) > 0:
            values['contents'] = [str(item.name) for item in self.contents]
        return str(values)

class ToDo(Task):
    """ 
    Master list containing projects which then contain individual tasks
    """ 
    def __getitem__(self, index):
        return self.contents[index] 

    def list_contents(self):
        """
        Converts list of class instances into a list of strings
        """
        if len(self.contents) > 0:
            list_contents = [str(item.name) for item in self.contents]
            return list_contents
        else:
            return None

    def add(self, pname):
        """
        Adds a new project to the ToDo
        """
        if isinstance(pname, Project):
            self.contents.append(pname)
        else:
            self.contents.append(Project(pname))

    def next_steps(self):
        """
        Lists out just the next step in each project
        """
        return [item.next_step() for item in self.contents]

    def total_steps_taken(self):
        """
        Sums the total number of steps taken in each project.
        """
        for item in range(len(self.contents)):
            self.steps_taken +=self.contents[item].steps_taken
        return self.steps_taken

    def delete(self, arg):
        """
        Removes a project/task either by its index or name
        """
        if type(arg) == int:
            i = arg
        elif type(arg) == str:
            i = self.list_contents().index(arg)
        self.contents.pop(i)

class Project(ToDo):
    """
    Contains the individual tasks
    """
    def add(self, tname):
        """
        Adds a task to the project
        """
        if isinstance(tname, Task):
            self.contents.append(tname) 
        else:
            self.contents.append(Task(tname))

    def next_step(self):
        """
        Returns what the next step in the project is. Done by list order
        """
        return self.contents[0].name

    def take_step(self):
        """
        Checks off the next step in the project and adds to the steps counter
        """            
        if len(self.contents) > 0:
            self.steps_taken += 1
            self.contents.pop(0)
            return "You have taken {} steps! Keep going!".format(self.steps_taken)