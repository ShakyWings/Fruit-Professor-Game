isFruit = ["apple", "banana", "cherry", "durian", "fig", "guava", "mango", "lemon", "longan", "kiwi"]
fruitList = []
playerList = []
gameStart = True
playerCount = 0

numOfPlayer = int(input("How many players are there in total? "))
for x in range(numOfPlayer):
    player = input("Input Player " + str(x+1) + " 's name: ")
    playerList.append(player)

print("Welcome to the Fruit Professor Playoff!")
print("May the best fruitist win!")
while gameStart:
    print(playerList[playerCount % len(playerList)]+ "'s turn.")
    fruit = input("Enter a fruit name: ").lower()
    if fruit in isFruit:
        if fruit in fruitList:
            print(fruit, "is already in the list.")
            print(playerList[playerCount % len(playerList)], "has lost!")
            playerList.remove(playerList[playerCount % len(playerList)])
        else:
            fruitList.append(fruit)
            playerCount += 1
    else:
        print(fruit, "is not a fruit!")
        print(playerList[playerCount % len(playerList)],"has lost!")
        playerList.remove(playerList[playerCount % len(playerList)])
    if len(playerList) == 1:
        print(fruitList)
        print(playerList[0],"is our Fruits Professor!")
        gameStart = False