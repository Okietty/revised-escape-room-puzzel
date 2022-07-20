import random

def palidrome(thisString):
    length = len(thisString) // 2

    left = 0
    right = len(thisString)
    palidromeChecker = 0

    for i in range(length):
        if thisString[left] == thisString[right - 1]:
            left += 1
            right -= 1
            palidromeChecker += 1


    if palidromeChecker == length:
        return(True)
    else:
        return(False)


def DecToBin(decimal):
    binaryList = []
    while decimal != 0:
        if decimal % 2 == 0:
            binaryList.append(0)
            decimal //= 2
        else:
            binaryList.append(1)
            decimal //= 2

    print(binaryList)



goldCounter = 0
numOfTries = 1


#First Game


print('Hello, welcome to the escape room. You will face a multitude of puzzels which you will have to solve. In order to escape, you must come out with atleast 4 gold in your gold')
print('counter, or you will die. You will be given three chances for each puzzel, if you fail to solve one in that many tries, you will be forced to move onto the next. Enjoy!')

print('')
print('     First puzzel, ONE LIKE THE OTHER!')
print('Here are some words, type in a a word that is common between these: radar | kayak | civil | deified | racecar')

while numOfTries != 4:
    firstGameUser = palidrome(input("Answer: ").lower())
    if firstGameUser == True:
        print('Congratulations, this puzzel was all about palidromes')
        goldCounter += 1
        break
    else:
        print('Ohhhhh, no, this is try number:', numOfTries)
        numOfTries += 1

numOfTries = 1


#Second Game


print('')
print('     Second puzzel, ON AND ON FROM THERE!')
print('Give the next five digits in the following sequence: 13 21 34 55 89 144 _ _ _ _ _')

while numOfTries != 4:
    secondGameUser = (input("Answer: "))
    if secondGameUser == '233 377 610 987 1597':
        print('Congratulations, this puzzel was all about the fibonacci sequence')
        goldCounter += 1
        break
    else:
        print('Ohhhhh, no, this is try number:', numOfTries)
        numOfTries += 1

numOfTries = 1


#Decision


print('')
decisionUser = input("Now, for the once in a life time offer, you can either skip the next puzzel, or get one free gold. To skip, say 'skip', for the extra gold, say 'gold': ")


#Third Game


randomBinNum = random.randint(0, 255)

if decisionUser == 'gold':
    print('')
    print('     Hahahaha, you have been tricked, their is no gold here, just another puzzel. Welcome to the......')
    print('     Third puzzel, THIS THAT!')
    print('While us humans use the decimal number system, comuters use the binart number system, meaning they can oly interpret through 1s and 0s. Now its your turn.')
    print('A given binary will be shown and you have to decipher it to its decimal value.')
    print('The number you have to decipher it')
    DecToBin(randomBinNum)

    while numOfTries != 4:
        thirdGameUser = int((input("Answer: ")))
        if thirdGameUser == randomBinNum:
            print("Congratulations, now you know how to speak in a computer's language")
            goldCounter += 1
            break
        else:
            print('Ohhhhh, no, this is try number:', numOfTries)
            numOfTries += 1

    numOfTries = 1


#Fourth Game


print('')
print('     Next puzzel, WHERE IS MY ORDER?!')
menuList = ['Cheese : 1', 'Taco : 2', 'Hotdog : 3']
toppingList = ['Cheese : 1', 'Onion : 2', 'Beef : 3', 'Tomatoes : 4', 'Refined beans : 5', 'Ketchup : 6', 'Lettuce : 7', 'Rice : 8', 'Avacado : 9']
print('Our menu', menuList)
print('Our toppings', toppingList)
print('Hello, this is the office of a very important buisness owner, I would like to place an order for: A Taco with ketchup, beef, avacodo, and extra ketchup')

while numOfTries != 4:
    fourthGameUser = (input("Place the order: "))
    if fourthGameUser == '2 6 3 9 6':
        print('Congratulations, the buisness owner is pleased with his order and tips you a gold')
        goldCounter += 1
        break
    else:
        print('Ohhhhh, no, this is try number:', numOfTries)
        numOfTries += 1

numOfTries = 1


#Fifth Game


randomNumGenerated = random.randint(3, 18)

print('')
print('     Final puzzel, ROLL OF THE DICE!')
print('Welcome to the final game, and it all ahs to do with you luck. A randomly generated number will be given to you and you will roll three dices that have')
print('to add up to that number. I hope you brang you lucky charm because you will need it')
print('Your number is:', randomNumGenerated)

while numOfTries != 4:
    fifthGameUser = (input("Type 'roll' to roll: "))
    if fifthGameUser == 'roll':
        randomNum1 = random.randint(1, 6)
        randomNum2 = random.randint(1, 6)
        randomNum3 = random.randint(1, 6)
        print(randomNum1)
        print(randomNum2)
        print(randomNum3)
        addedRolls = randomNum1 + randomNum2 + randomNum3
    if addedRolls == randomNumGenerated:
        print('Congratulations, it appears you are luckier than you think')
        goldCounter += 1
        break
    else:
        print('Ohhhhh, no, this is try number:', numOfTries)
        numOfTries += 1


#Count up


print('')
print('')
print('')
print('')
print("After tallying up all your gold, it appears that.......")
if goldCounter >= 4:
    print('You have escape, congratualtions, having', goldCounter, 'gold')
else:
    print('You did not escape, you had', goldCounter, 'gold')
