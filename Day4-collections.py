from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

# This is a standard tuple
user = ('bob', 'coder')

# now lets build a named tuple

User = namedtuple('User', 'name role')
user = User(name='Jolynn', role='coder')
print(user.name)
print(user.role)

print(user.name + " is a " + user.role)

# This is a standard dictionary

usersD = {'bob':'coder'}
print(usersD.get('bob'))
usersD.get('julian') is None

challenges_done = [('jolynn', 10), ('julian', 7), ('bob', 5),
                   ('jolynn', 11), ('julian', 8), ('bob', 6)]

print(challenges_done)

#change it to a defaultdict
# we define list since we will be making a list of challenges done
# it can initilize the type for you
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)

# now lets look at counter

words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
print(words[:5])

# no need to loop over it to count when you have counter

mostCommon = Counter(words).most_common(5)
print(mostCommon)

