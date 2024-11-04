voted = dict()


def check_voted(name):
  if voted.get(name):
    print("kick them out")
  else:
    voted[name] = True
    print("let them vote!")

while True:
  name = input("Enter your name: ")
  check_voted(name)
