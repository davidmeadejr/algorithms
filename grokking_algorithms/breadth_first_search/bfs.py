from collections import deque

"""
Pattern: Breadth-First Search (BFS)

Solution: Initialize a queue with people to check and a list of those already checked; while the queue isn’t empty, remove the first person, check if they’re a mango seller (returning True if so), otherwise add their friends to the queue and mark them as checked; return False if no seller is found. 

"""
 
 graph = {
  "you": ["alice", "bob", "claire"],
  "alice": ["peggy"],
  "bob": ["anuj", "peggy"],
  "claire": ["thom", "jonny"],
  "anuj": [],
  "peggy": [],
  "thom": [],
  "jonny": [],
}

def mango_seller(name):
  return name == "David"

def search(name):
  queue = deque()
  queue += graph[name]
  people_already_asked_ls = []

  while queue:
    person_in_question = queue.popleft()
    if person_in_question not in people_already_asked_ls:
      if mango_seller(person_in_question):
        return person_in_question + " is a mango seller!"
      else:
        queue += graph[person_in_question]
        people_already_asked_ls.append(person_in_question)
  return "Sorry, looks like there are no mango seller the nearby area."
print(search("you"))  