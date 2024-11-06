print("Nice Old Affirmation Machine")

name = input("Who are you? ")
print("Hey", name)
day = input("What day is it? ")
if day == "Monday" or day == "monday":
  print("Monday's are the worst, but I hope you have a great day!")
elif day == "Tuesday" or day == "tuesday":
  print("Tuesday's are a bit better, and I hope you have a great day!")
elif day == "Wednesday" or day == "wednesday":
  print("Wednesday's are for bosses, and I hope you have a great day!")
elif day == "Thursday" or day == "thursday":
  print("Thursday's are for the dudes, and I hope you have a great day!")
elif day == "Friday" or day == "friday":
  print("Friday's are for the ladies, and this is Our day!")
hair = input("How much air do you have on your head? ")
if hair == "a lot":
  print("That's amazing!")
  feelings = input("On a scale of 1 - 10 how do you feel today? (1: 😭, 10: 🥳) ")
  if feelings == "1":
    print("Hey", name, """keep your chin up! Today you're going to Teach people to       code. Time to jump up like a baby! In the most amazing way, simply by being        you - YOU ROCK!""")
  elif feelings == "5":
    print("Hey", name, """you're almost there! Keep up the good work! You're going       to Teach people to code. Time to do what you love doing best.""")
  else:
    print("Hey", name, """there you go! You're doing great! Keep up the good work!     You're going to Teach people to code. Have a pat on your back for the good job.
    """)
else:
  print("grow some hair")
  
