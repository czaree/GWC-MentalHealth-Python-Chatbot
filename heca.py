#external modules
import time
import datetime
import random
#typing animation
def wait_animation():
  think = ["", ".", "..", "...", "...."]
  i = 0
  for x in range(5):
    print("\033[3mheca is typing" + think[i % len(think)] + "\033[0m", end="\r")
    time.sleep(.45)
    i += 1
#script only runs if selected from main.py
if __name__ == "__main__":
  #intro sequence
  wait_animation()
  print("hey! i'm heca, and i'd like to be your friend!! :)")
  wait_animation()
  print("i was created as a part of an initiative to better people's mental health.")
  wait_animation()
  name = str(input("before we get started, tell me, what's your name?\n"))
  #advice arrays - selects emotion mentioned in response and randomizes the reply from a few options, values defined before they can be used
  greet = [name + ", huh? i'll have to remember that. i think it really suits you.", "nice to meet you " + name + "!"]
  emotions = ["sad", "angry", "happy", "anxious", "depressed", "mad", "frustrated"]
  sad_advice = ["I'm sorry to hear that " + name + ". try setting aside some time for yourself to relax. i'd suggest do something you love to take your mind off it for a bit.", "that must've been really hard to deal with today. it might help to talk to a friend or loved one to ease some of the tension you might be feeling. or, personally if i don't feel like being around other people, i like to journal out my thoughts instead.", "i'm here for you. life can be really difficult at times. take life one step at a time, no matter how small, for however long you need to."]
  angry_advice = ["sometimes life can throw you a curve ball, and nothing seems to go your way. do whatever you feel like you need to let some of that anger out. whether it be ripping up paper, going for a run, or screaming until you can't anymore, there isn't really any bad ways to express how you feel. The important part is that you don't bottle up your emotions and try to hide them.", "In the heat of the moment it's really easy to lose your temper. Whatever the reason, your anger is valid, but be sure to take a step back and collect your thoughts before you speak. Unrestrained anger can cause a person to lash out and hurt others, even if they didn't mean to.", "If you feel like you're being driven up the wall by focusing too much on your own emotions, try to reframe the situation and think of potential solutions to your problem. Anger is often justified, but won't help you ease any of the actual tension, sometimes even making the situation worse. Of course, not every problem can be resolved easily, but consider what you can do to make the situation more bearable."]
  happy_advice = ["glad you're feeling good! make sure to get plenty of rest to keep the ball rolling.", "that's great! keep up the good work! nothing can stop you now :)", "i'm proud of you!! i hope the rest of your week is just as great!"]
  frustrated_advice = ["it's okay to mess up or be unable to do things sometimes. if you're too oent up and angry, nothing good will come out of it. take a step back, take a deep breath, and reevalute whether to come back to the issue another time, or let it go. things will turn out alright.", "its okay to just do the bare minimum sometimes. don't get caught up too much in the small details of things if it feels like a burden. perfection is appreciated, but never expected.", "don't be afraid to be kind to yourself. whatever you're going through, its likely an insane amount of stress. it's okay to take a break and do something you enjoy! if it's all too much, circle back to it another time"]
  wait_animation()
  print(greet[random.randrange(0, 3, 1)])
  wait_animation()
  #advice output - asks how the user is feeling and prints the randomized response
  while True:
    feeling = input("so tell me, how are you feeling today?\n")
    if emotions[0] in feeling or emotions[4] in feeling:
      sad_choose = sad_advice[random.randrange(0, 3, 1)]
      wait_animation()
      print(sad_choose)
      break
    elif emotions[1] in feeling or emotions[5] in feeling:
      angry_choose = angry_advice[random.randrange(0, 3, 1)]
      wait_animation()
      print(angry_choose)
      break
    elif emotions[2] in feeling:
      happy_choose = happy_advice[random.randrange(0, 3, 1)]
      wait_animation()
      print(happy_choose)
      break
    elif emotions[6] in feeling:
      frustrated_choose = frustrated_advice[random.randrange(0, 3, 1)]
      wait_animation()
      print(frustrated_choose)
      break
    else:
      wait_animation()
      print("sorry, I don't think i understand that. try telling me again, maybe using some different words?")
  #
  
  #end sequence
  wait_animation()
  #time-based goodbye message
  morning_string = "5:00:00"
  afternoon_string = "12:00:00"
  evening_string = "17:00:00"
  night_string = "22:00:00"
  midnight_string = "23:59:59"
  midnightmorn_string = "00:00:00"
  #usertime_string = "6:00:00"
  time_bye = ""
  #user_time = datetime.datetime.strptime(usertime_string, "%H:%M:%S").time()
  user_time = datetime.datetime.now().time()
  morning_time =   datetime.datetime.strptime(morning_string, "%H:%M:%S").time()
  afternoon_time = datetime.datetime.strptime(afternoon_string, "%H:%M:%S").time()
  evening_time = datetime.datetime.strptime(evening_string, "%H:%M:%S").time()
  night_time = datetime.datetime.strptime(night_string, "%H:%M:%S").time()
  midnight_time = datetime.datetime.strptime(midnight_string, "%H:%M:%S").time()
  midnightmorn_time = datetime.datetime.strptime(midnightmorn_string, "%H:%M:%S").time()
  if user_time >= morning_time and user_time < afternoon_time:
    time_bye = "thanks for stopping by, have a good rest of your morning!"
  if user_time >= afternoon_time and user_time < evening_time:
    time_bye = "it was nice to hear from you today, see you later! have a great afternoon :)"
  if user_time >= evening_time and user_time < night_time:
    time_bye = "it was great to see you today! take care, have a pleasant evening."
  if user_time >= night_time and user_time < midnight_time:
    time_bye = "it was really nice talking with you, but it's getting late, so good night! be sure to get some rest"
  if user_time >= midnightmorn_time and user_time < morning_time:
    time_bye = "it was great meeting you today! it's pretty early in the morning for you though, right? try and get some sleep if you can. goodnight!"
  #else:
    #time_bye = "error. whoopsies lol"
  goodbyes = [time_bye, time_bye, time_bye, "thanks for chatting with me! I'll catch you later", "i had a great time chatting today, hope to see you again sometime soon!", "i'm really glad that i got to talk to you today, see you later!"]
  print(goodbyes[random.randrange(0, 2, 1)])