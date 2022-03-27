import random

def TellAJoke():
	num = random.randint(0, 2)
	if(num == 0):
		input("Let me tell you a joke to cheer you up!\nHow many programmers does it take to change a lightbulb?\n")
		print("None, that's a hardware problem.")
	elif(num == 1):
		input("What do you call 8 Hobbits?\n")
		print("A Hobbyte.")
	else:
		input("What are the two hardest problems in Computer Science?\n")
		print("Cache Invalidation, Naming Things, and Off-By-One Errors.")

def give_advice():
	num = random.randint(0, 2)
	if(num == 0):
		print("I would recommend considering some healthy methods to express and release your emotions. " \
	  + "Personally, I go on long walks or busy myself with a hobby that will cheer me up when I'm sad!")
	elif(num == 1):
		print("There are manys ways " \
		+ "of expressing your sadness and releasing it, " \
		+ "so long as it is a healthy method!")
	else:
		print("Certain things/activities are associated with dopamine, aka happiness. That's why watching a movie, playing videogames, etc. makes you happy.")
#script only runs if chosen from main.py
if __name__ == "__main__":
  username = input("Welcome! Enter your name: ")
  print("Hi, " + username + "! I am a Mood Solver Robot. " \
  + "Tell me how you feel" \
  + " and I'll do my best to help!")
  
  current_mood = input("What would you rate your mood today out of 5?\n") 
  while not (current_mood.isdigit()):
  	current_mood = input("That's not in the range! Try again:\n")
  
  info = input("Tell me something about yourself.\n")
  
  num = random.randint(0, 2)
  if(num == 0):
    print("Really? Wow!")  
  elif(num == 1):
    print("No kidding.")
  else:
    print("That's quite interesting.")
    
  info = input("What do you think will help you cheer up the most? (FACT, JOKE, ADVICE, DONE)\n")
  info = info.upper()
    
  while info != "DONE":
    if(info == "FACT"):
      print("Sadness is caused by the lack of chemicals that provide happiness in the brain. An excess lack of said chemical can lead to chronic depression.")
    elif(info == "JOKE"):
      TellAJoke()
    elif(info == "ADVICE"):
      give_advice()
    else:
      print("Nevermind...")
  	
    info = input("What do you think will help you cheer up the most? (FACT, JOKE, ADVICE, DONE):\n")
    info = info.upper()