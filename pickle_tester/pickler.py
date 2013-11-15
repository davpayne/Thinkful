import sys
import pickle

def list_pickler(a_list, path):
	fil = open(path, 'wb')
	pickle.dump(a_list, fil)
	fil.close()

def unpickler(path):
	fil = open(path, 'rb')
	b_list = pickle.load(fil)
	fil.close()
	return b_list