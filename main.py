import os
import time
import shutil
#local files
import SashaExtraCode
import heca
#clear the screen
def clear():
  os.system("cls||clear")
#possible start up animation?
def initialize():
  init_animation = [
  "||                 ||",
  "|||               |||",
  "||||             ||||",
  "|||||           |||||",
  "||||||         ||||||",
  "|||||||       |||||||",
  "||||||||     ||||||||",
  "|||||||||   |||||||||",
  "|||||||||| ||||||||||",
  "|||||||||||||||||||||",
  "|||||||||||||||||||||",
  "||||||||||d||||||||||",
  "|||||||||nd |||||||||",
  "||||||||and W||||||||",
  "||||||| and We|||||||",
  "||||||o and Wel||||||",
  "|||||lo and Welc|||||",
  "||||llo and Welco||||",
  "|||ello and Welcom|||",
  "||Hello and Welcome||"
]
  i = 0
  for x in range(20):
    print(init_animation[i % len(init_animation)],  end="\r")
    #print(init_animation[i % len(init_animation)].center(shutil.get_terminal_size().columns),  end="\r")
    #BUG - using shutil to center the animation does weird things to the display, apply w/ caution
    time.sleep(.07)
    i += 1
  print("||Hello and Welcome||")
  print("")
  #print("||Hello and Welcome||".center(shutil.get_terminal_size().columns))
#options menu animation
def settings_start():
    sett_animation = [
    "||        ||",
    "|||      |||",
    "||||    ||||",
    "|||||  |||||",
    "||||||||||||",
    "||||||||||||",
    "|||||ti|||||",
    "||||ttin||||",
    "|||etting|||",
    "||Settings||"
    ]
    i = 0
    for x in range(10):
      print(sett_animation[i % len(sett_animation)],  end="\r")
      #print(init_animation[i % len(init_animation)].center(shutil.get_terminal_size().columns),  end="\r")
      #BUG - using shutil to center the animation does weird things to the display, apply w/ caution
      time.sleep(.07)
      i += 1
    print("||Settings||")
    print("")
#program choice
while True:
  initialize()
  time.sleep(.75)
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
  elif "setting" in choice_program:
    clear()
    settings_start()
    break
  else:
    print("That is not a valid program name. Please try again.")
    time.sleep(2)
    clear()
