import os
import time
#local files
import SashaExtraCode
import heca
#clear the screen
def clear():
  os.system("cls||clear")
#program choice
while True:
  print("== Hello and Welcome, USER. ==")
  choice_program = input("Would you like to load the Mood Solver Robot, or the HECA initiative?\n")
  choice_program = choice_program.lower()
  if "heca" in choice_program:
    clear()
    exec(open("heca.py").read())
    break
  elif "mood" in choice_program:
    clear()
    exec(open("SashaExtraCode.py").read())
    break
  else:
    print("That is not a valid program name. Please try again.")
    time.sleep(2)
    clear()
    