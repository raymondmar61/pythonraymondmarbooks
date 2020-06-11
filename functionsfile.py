def formattedname(x, y):
	return (x+" "+y).title()

class AnonymousSurvey():
	"""Collect anonymous answers to a survey question"""
	def __init__(self, question):
		self.question = question
		self.listresponses = []
	def displayquestion(self):
		print(self.question)
	def saveresponse(self, addresponse):
		self.listresponses.append(addresponse)
	def showresponse(self):
		print("The list",self.listresponses)
		print("Your languages are {}".format(", ".join(self.listresponses)))
		isitworking = (", ".join(self.listresponses))
		print(isitworking)
