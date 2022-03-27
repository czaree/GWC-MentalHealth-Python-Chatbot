import os
#local files
import SashaExtraCode
import heca
#clear the screen
def clear():
  os.system("cls||clear")
#program choice
while True:
  choice_program = input("Would you like to load the Mood Solver Robot, or the HECA initiative?\n")
  if "heca" in choice_program or "HECA" in choice_program:
    clear()
    exec(open("heca.py").read())
    break
  elif "mood" in choice_program or "Mood" in choice_program:
    clear()
    exec(open("SashaExtraCode.py").read())
    break
  else:
    print("That is not a valid program name. Please try again.")
    