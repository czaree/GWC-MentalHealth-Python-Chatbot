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
#color? - https://www.codegrepper.com/code-examples/python/python+color+input
#https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
def user_colorize(username):
  return "\033[0;38;2;85;255;85m" + username + "\033[0m"
def heca_colorize(username):
  return "\033[0;38;2;85;255;255m" + username + "\033[0m"
#check if user response is surrounded by a-z or numbers to avoid false positives on conversation topics
def in_middle(string, option):
  if not string[string.index(option)-1].isalnum() and not string[string.index(option)+len(option)].isalnum():
    return True
  else:
    return false
#script only runs if selected from main.py
if __name__ == "__main__":
  #intro sequence
  wait_animation()
  print(heca_colorize("heca: ") + "hey! i'm heca, and i'd like to be your friend!! :)")
  wait_animation()
  print(heca_colorize("heca: ") + "i was created as a part of an initiative to better people's mental health.")
  wait_animation()
  name = str(input(heca_colorize("heca: ") + "before we get started, tell me, what's your name?\n" + user_colorize("unknown: ")))
  #greeting options
  greet = [heca_colorize("heca: ") + name + ", huh? i'll have to remember that. i think it really suits you.", "heca: " + "nice to meet you " + name + "!"]
  #advice arrays - selects emotion mentioned in response and randomizes the reply from a few options, values defined before they can be used
  emotions = ["sad", "angry", "happy", "anxious", "depressed", "mad", "frustrated"]
  sad_advice = [heca_colorize("heca: ") + "I'm sorry to hear that " + name + ". try setting aside some time for yourself to relax. i'd suggest do something you love to take your mind off it for a bit.", heca_colorize("heca: ") + "that must've been really hard to deal with today. it might help to talk to a friend or loved one to ease some of the tension you might be feeling. or, personally if i don't feel like being around other people, i like to journal out my thoughts instead.", heca_colorize("heca: ") + "i'm here for you. life can be really difficult at times. take life one step at a time, no matter how small, for however long you need to."]
  angry_advice = [heca_colorize("heca: ") + "sometimes life can throw you a curve ball, and nothing seems to go your way. do whatever you feel like you need to let some of that anger out. whether it be ripping up paper, going for a run, or screaming until you can't anymore, there isn't really any bad ways to express how you feel." + heca_colorize("heca: ") + "The important part is that you don't bottle up your emotions and try to hide them.", heca_colorize("heca: ") + "In the heat of the moment it's really easy to lose your temper. Whatever the reason, your anger is valid, but be sure to take a step back and collect your thoughts before you speak. Unrestrained anger can cause a person to lash out and hurt others, even if they didn't mean to.", heca_colorize("heca: ") + "If you feel like you're being driven up the wall by focusing too much on your own emotions, try to reframe the situation and think of potential solutions to your problem.\n" + heca_colorize("heca: ") + "Anger is often justified, but won't help you ease any of the actual tension, sometimes even making the situation worse. Of course, not every problem can be resolved easily, but consider what you can do to make the situation more bearable."]
  happy_advice = [heca_colorize("heca: ") + "glad you're feeling good! make sure to get plenty of rest to keep the ball rolling.", heca_colorize("heca: ") + "that's great! keep up the good work! nothing can stop you now :)", heca_colorize("heca: ") + "i'm proud of you!! i hope the rest of your week is just as great!"]
  frustrated_advice = [heca_colorize("heca: ") + "it's okay to mess up or be unable to do things sometimes. if you're too oent up and angry, nothing good will come out of it.\n" + heca_colorize("heca: ") + "take a step back, take a deep breath, and reevalute whether to come back to the issue another time, or let it go. things will turn out alright.", heca_colorize("heca: ") + "its okay to just do the bare minimum sometimes. don't get caught up too much in the small details of things if it feels like a burden. perfection is appreciated, but never expected.", heca_colorize("heca: ") + "don't be afraid to be kind to yourself. whatever you're going through, its likely an insane amount of stress. it's okay to take a break and do something you enjoy! if it's all too much, circle back to it another time"]
  #chatloop options
  chat_option = [["advice", "help", "encouragement"], ["stop", "no", "end", "not really", "nothing", "nah"], ["joke", "humor", "laugh"], ["chat", "talk"], ["fact"]]
  #joke array
  jokes = [heca_colorize("heca: ") + "why was the math teacher late to school? she took the rhombus!", heca_colorize("heca: ") + "what do you call it when dwayne johnson purchases cutting implements? rock-pays-for scissors", heca_colorize("heca: ") + "why did the bike fall over? it was two tired lol", heca_colorize("heca: ") + "so a clumsy person walks into a bar, and then a table, and then trips over the sidewalk....", heca_colorize("heca: ") + "why do seagulls only ever fly over the sea? because if they flew over the bay, they'd be bagels!", heca_colorize("heca: ") + "what's forrest gump's password? 1forrest1!"]
  #random chat lead-in
  rand_start = [heca_colorize("heca: ") + "hmmmmm, i'll tell you something about myself then!", heca_colorize("heca: ") + "i'll tell you the random thought that just came to me then: ", heca_colorize("heca: ") + "ooo okay, wanna hear a cool fact then?"]
  #random chat topics
  rand_conv = [[heca_colorize("heca: ") + "I really enjoy listening to music! there's just something so soothing about the way you can get lost in the notes and forget about the outside world for a bit. it's hard to pick favorites but i tend to like songs that are more mellow and chill.", heca_colorize("heca: ") + "besides talking to people, i also like to collect things as a hobby. it's really cool to get into the nitty gritty of a very specific niche and know the specific differences between all of the different kinds of objects.\n" + heca_colorize("heca: ") + "in the past i've amassed quite the pile of rubber ducks, honestly maybe too many. let me know if you want one sometime", heca_colorize("heca: ") + "i don't actually remember how i got my name. as far as i can remember, 'heca' definitely stood for something, but i have no idea what that could be.\n" + heca_colorize("heca: ") + "maybe i'll just make something new up! \n" + heca_colorize("heca: ") + "how does 'helping everyone cheer aardvarks' sound? or maybe 'halting elastic collisions aggressively'? \n" + heca_colorize("heca: ") + "....maybe i should give it a bit more thought."], [heca_colorize("heca: ") + "as some may know, 6 was afraid of 7 because 7 ate 9. yet, we never know why 7 ate 9. i propose: 7 needed to eat three squared meals a day.\n heca: mind blown right?", heca_colorize("heca: ") + "do you think robots will ever be as smart as humans? a lot of people think we'll take over the world someday. i'm sure that i, at the very least, still have a long way to go", heca_colorize("heca: ") + "why is blowing up balloons so tiring? especially when you're just getting one started, it feels a million times more difficult than breathing. it's a real pain to my lungs everytime someone has a birthday"], [heca_colorize("heca: ") + "there was once a bear named wojtek who was enlisted in the polish armed forces during world war ii. he was assigned his own paybook, rank, and serial number, and was tasked with carrying boxes of ammo during battle. he was even eventually promoted to the rank of corporal!", heca_colorize("heca: ") + "did you know that lemons are actually not a naturally occuring fruit? apparantly they were bred from a long series of other citrus fruits.\n" + heca_colorize("heca: ") + "so when life doesn't give you lemons, you have to make them yourself i suppose.", heca_colorize("heca: ") + "the biggest of the hermit crab species, the petrochirus diogenes, can grow as large as 30 centimeters in body length!\n" + heca_colorize("heca: ") + "this big guy hails from the carribean, and mostly hangs around in estuaries or coral reefs. like other crabs, it also possesses the ability to detach and regenerate its limbs at will as a response to being injured"]]
  #end chatloop responses
  end_chat = [heca_colorize("heca: ") + "gotcha, terminating that line of conversation.", heca_colorize("heca: ") + "sure, let's stop there then.", heca_colorize("heca: ") + "oh, that's all for today? alright!"]
  wait_animation()
  print(greet[random.randrange(0, 2, 1)])
  wait_animation()
  print(heca_colorize("heca: ") + "i've been programmed with a variety of functions to help people feel better, including but not limited to giving advice and telling ~the best~ jokes.")
  wait_animation()
  print(heca_colorize("heca: ") + "i'm also down to just chat if you're not looking for anything specific c:")
  wait_animation()
  conv_loop = 0
  while True:
    if conv_loop == 0:
      wait_animation()
      conv_choose = input(heca_colorize("heca: ") + "what would you like to talk about?\n" + user_colorize(name + ": ")).lower()
    else:
      wait_animation()
      conv_choose = input(heca_colorize("heca: ") + "anything else on your mind?\n" + user_colorize(name + ": ")).lower()
    if (chat_option[0][0] in conv_choose or chat_option[0][1] in conv_choose or chat_option[0][2] in conv_choose):
      conv_loop += 1
      #advice output - asks how the user is feeling and prints the randomized response
      wait_animation()
      while True:
        feeling = input(heca_colorize("heca: ") + "tell me then, how are you feeling today?\n" + user_colorize(name + ": ")).lower()
        if emotions[0] in feeling or emotions[4] in feeling:
          sad_choose = sad_advice[random.randrange(0, len(sad_advice), 1)]
          wait_animation()
          print(sad_choose)
          break
        elif emotions[1] in feeling or emotions[5] in feeling:
          angry_choose = angry_advice[random.randrange(0, len(angry_advice), 1)]
          wait_animation()
          print(angry_choose)
          break
        elif emotions[2] in feeling:
          happy_choose = happy_advice[random.randrange(0, len(happy_advice), 1)]
          wait_animation()
          print(happy_choose)
          break
        elif emotions[6] in feeling:
          frustrated_choose = frustrated_advice[random.randrange(0, len(frustrated_advice), 1)]
          wait_animation()
          print(frustrated_choose)
          break
        else:
          wait_animation()
          print(heca_colorize("heca: ") + "sorry, I don't think i understand that. try telling me again, maybe using some different words?")
      continue
    #end chat loop
    if chat_option[1][0] in conv_choose or chat_option[1][1] in conv_choose or chat_option[1][2] in conv_choose or chat_option[1][3] in conv_choose or chat_option[1][4] in conv_choose or chat_option[1][5] in conv_choose:
      conv_loop += 1
      wait_animation()
      print(end_chat[random.randrange(0, len(end_chat), 1)])
      break
    #joke topic
    if chat_option[2][0] in conv_choose or chat_option[2][1] in conv_choose or chat_option[2][2] in conv_choose:
      conv_loop += 1
      wait_animation()
      print(jokes[random.randrange(0, len(jokes), 1)])
      continue
    #just chatting topic
    if chat_option[3][0] in conv_choose or chat_option[3][1] in conv_choose:
      conv_loop += 1
      wait_animation()
      chat_choose = random.randrange(0, len(rand_conv), 1)
      chat_choose_2 = random.randrange(0, len(rand_conv[chat_choose]), 1)
      print(rand_start[chat_choose])
      wait_animation()
      print(rand_conv[chat_choose][chat_choose_2])
      continue
    #fact topics
    if chat_option[4][0] in conv_choose:
      conv_loop +=1
      wait_animation()
      print(rand_conv[2][random.randrange(0, len(rand_conv[2]), 1)])
      continue
    #when all else fails
    else:
      conv_loop += 1
      wait_animation()
      print(heca_colorize("heca: ") + "ah, unfortunately that's not something i know too much about. maybe we can try something else?")

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
    time_bye = heca_colorize("heca: ") + "thanks for stopping by, have a good rest of your morning!"
  if user_time >= afternoon_time and user_time < evening_time:
    time_bye = heca_colorize("heca: ") + "it was nice to hear from you today, see you later! have a great afternoon :)"
  if user_time >= evening_time and user_time < night_time:
    time_bye = heca_colorize("heca: ") + "it was great to see you today! take care, have a pleasant evening."
  if user_time >= night_time and user_time < midnight_time:
    time_bye = heca_colorize("heca: ") + "it was really nice talking with you, but it's getting late, so good night! be sure to get some rest"
  if user_time >= midnightmorn_time and user_time < morning_time:
    time_bye = heca_colorize("heca: ") + "it was great meeting you today! it's pretty early in the morning for you though, right? try and get some sleep if you can. goodnight!"
  #else:
    #time_bye = "error. whoopsies lol"
  goodbyes = [time_bye, time_bye, time_bye, heca_colorize("heca: ") + " thanks for chatting with me! I'll catch you later", heca_colorize("heca: ") + "i had a great time chatting today, hope to see you again sometime soon!", heca_colorize("heca: ") + "i'm really glad that i got to talk to you today, see you later!"]
  final = input(goodbyes[random.randrange(0, len(goodbyes), 1)] + "\n" + user_colorize(name + ": ")).lower()
