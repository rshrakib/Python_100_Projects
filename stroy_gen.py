import random
when = ['a few years ago', 'yesterday', 'last night', 'a long time ago', 'an 20th jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Rakib', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'Bangladesh', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']


print(random.choice(when)+ "," + random.choice(who) + " that lived in " + random.choice(residence) + " went to the "+ random.choice(went) + ' and ' + random.choice(happened))
