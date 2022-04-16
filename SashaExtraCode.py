import random
def TellAJoke():
	num = random.randint(0, 2)
	if(num == 1):
		input("let me tell you a joke to cheer you up!\nhow many programmers does it take to change a lightbulb?\n")
		print("none, that's a hardware problem")
	elif(num == 2):
		input("what do you call eight hobbits?\n")
		print("a hobbyte")
	else:
		input("what are the two hardest problems in computer science?\n")
		print("cache invalidation, naming things, and off-by-one errors")

def give_advice():
	num = random.randint(0, 2)
	if(num == 1):
		print("i would recommend considering some healthy methods to express and release your emotions. " \
	  + "personally, i go on long walks or busy myself with a hobby that will cheer me up when i'm sad (ignore that i am a robot that cannot move whatsoever")
	elif(num == 2):
		print("there are manys ways " \
		+ "of expressing your sadness and releasing it, " \
		+ "so long as it is a healthy method")
	else:
		print("certain things/activities are associated with dopamine, aka happiness. that's why watching a movie or playing videogames makes you happy")
#script only runs if chosen from main.py
if __name__ == "__main__":
  username = input("welcome! please enter your name: ")
  print("hi, " + username + "! i'm a mood solver robot. " \
  + "tell me how you feel" \
  + " and i'll do my best to rid you of your sadness (if you possess any)")
  
  current_mood = input("what would you rate your mood today out of 5?\n") 
  while not (current_mood.isdigit()):
  	current_mood = input("sorry, but that's not in the range. try again:\n")
  
  info = input("i'll try my best to get rid of your sadness, whether or not it's a big or small amount. but before we get to that, tell me something cool about yourself :)\n")
  
  num = random.randint(0, 2)
  if(num == 1):
    print("really? wow!")  
  elif(num == 2):
    print("no kidding")
  else:
    print("hmm, that's quite interesting")
    
  info = input("what do you think will help you cheer up the most? (FACT, JOKE, ADVICE, DONE)\n")
  info = info.upper()
    
  while info != "DONE":
    if(info == "FACT"):
      print("sadness is caused by the lack of chemicals that provide happiness in the brain. an excess lack of said chemical can lead to chronic depression. this is a very watered-down explanation, so i would highly recommend doing some of your own research if you're interested")
    elif(info == "JOKE"):
      TellAJoke()
    elif(info == "ADVICE"):
      give_advice()
    else:
      print("nevermind...")
  	
    info = input("what do you think will help you cheer up the most? (FACT, JOKE, ADVICE, DONE):\n")
    info = info.upper()