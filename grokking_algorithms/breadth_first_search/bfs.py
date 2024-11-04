from collections import deque

"""
Pattern: Breadth-First Search (BFS)

Solution: Initialize a queue with people to check and a list of those already checked; while the queue isn’t empty, remove the first person, check if they’re a mango seller (returning True if so), otherwise add their friends to the queue and mark them as checked; return False if no seller is found. 

"""
# Implementation: 3


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

def person_is_seller(name):
  return name == "anuj"

def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        return person + " is a mango seller!"
      else:
        search_queue += graph[person]
        searched.append(person)
  return "There is no mango sellers :("

print(search("you"))  