print("Welcome to the Quiz Game")

playing = input("Would you like to play this game? ")

if playing != 'yes':
    quit()

print("Let us begin then!")
score = 0
# 1
answer = input("How many U.S. States are there? ")

if int(answer) == 50:
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is 50")
# 2
answer = input("Are Orcas whales or dolphins? ")

if answer.lower() == 'dolphin' or answer.lower() == 'dolphins':
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is dolphins")
# 3
answer = input("True or false, you can build a computer without a gpu? ")

if answer.lower() == 'true':
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is True")
# 4
answer = input("Are Java and JavaScript the same language? ")

if answer.lower() == 'no':
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is No")
# 5
answer = input("How many hours are in a week? ")

if int(answer) == 168:
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is 168")
# 6
answer = input("Who is the King of the gods in greek mythology? ").lower()

if answer == 'zeus':
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is Zeus")

# 7
answer = int(input("how many planets are in the solar system? "))

if answer == 8:
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is 8")

# 8
answer = input("Who is the leader of the Autobots ").lower()

if answer == 'optimus prime':
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is Optimus Prime")

# 9
answer = input("What sport does Lebron James play? ").lower()

if answer == 'basketball':
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is Basketball ")

# 10
answer = input("Who is Darth Vader under his mech suit? ").lower()

if answer == 'anakin skywalker':
    print('Correct!')
    score += 1
else:
    print("Sorry, the answer to the question is Anakin Skywalker")

print(f"Congratulations, you got a score of {(score/10)*100}")
