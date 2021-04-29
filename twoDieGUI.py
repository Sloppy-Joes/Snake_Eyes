from breezypythongui import EasyFrame
import random

class twoDieGUI(EasyFrame):
	"""Displays a greeting in a window."""

	def __init__(self):
		"""Sets up the window and widgets."""
		EasyFrame.__init__(self, title = "Two Dice", resizable = False, background = "firebrick4")
		
		self.addLabel(text = "Snake Eyes", row = 0, column = 0, columnspan = 3, sticky = "NSEW", background = "firebrick4", foreground= "yellow").config(font = ("Georgia", 20))
		
		self.first = self.addLabel(text="Player", row= 1, column= 0, background= "firebrick4", foreground= "white", sticky= "W").config(font = ("Georgia", 15))
				
		self.second = self.addLabel(text="Computer", row= 2, column= 0, background= "firebrick4", foreground= "black", sticky= "W").config(font = ("Georgia", 15))
		
		#self.numPanel = self.addPanel(row = 2, column = 0, background = "firebrick4", columnspan = 5)
		self.field1 = self.addIntegerField(value = 0, row = 1, column = 1, width = 3, sticky = "E")
		self.field11 = self.addIntegerField(value = 0, row = 1, column = 2, width = 3, sticky = "E")

		self.field2 = self.addIntegerField(value = 0, row = 2, column = 1, width = 3, sticky = "E")
		self.field22 = self.addIntegerField(value = 0, row = 2, column = 2, width = 3, sticky = "E")		

		self.addButton(text = "Roll Dice", row = 3, column = 0, columnspan = 5, command = self.pickNumbers)

		self.result = self.addTextField(text="Result", row = 4, column = 0, )

	def pickNumbers(self):
		playerRoll = random.randint(1, 6)
		computerRoll = random.randint(1, 6)

		if playerRoll > computerRoll:
			self.result.setText("You win!")
		elif playerRoll < computerRoll:
			self.result.setText("You lose.")
		else:
			self.result.setText("It\'s a tie.")

		# now take those random number variables and update the fields of the GUI
		self.field1.setNumber(playerRoll)
		self.field11.setNumber(playerRoll)
		self.field2.setNumber(computerRoll)
		self.field22.setNumber(computerRoll)


		

# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	twoDieGUI().mainloop()

# global call to the main() function
main()