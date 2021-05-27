import pickle
import os

class Menu():
	def __init__(self):
		try:
			# Open the menu pickle
			if os.path.getsize('menu.pickle')>0:
				with open('menu.pickle', 'rb') as pickle_in:
					self.menu = pickle.load(pickle_in)
					
		except Exception as e:
			pass

