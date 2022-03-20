from random import randrange


def intToHandChoice(choice):
    handMap = {
        0: "Rock",
        1: "Paper",
        2: "Scissors"
    }
    if choice in handMap:
        return handMap[choice]
    # error handle here?


def intToRoundResult(result):
    resultMap = {
        0: "Draw",
        1: "User Wins",
        2: "AI Wins"
    }
    if result in resultMap:
        return str(resultMap[result])
    # else error handle


def playHand(userChoice, aiChoice):
    doIWin = {
        0: 2,  # rock beats scissors
        1: 0,  # paper beats rock
        2: 1  # scissors beat paper
    }
    if doIWin[userChoice] == aiChoice:
        return 1
    else:
        return 2


def playRound(userChoice):
    aiChoice = randrange(3)
    print("AI chose " + intToHandChoice(aiChoice))
    if userChoice == aiChoice:
        return 0  # Draw
    return playHand(userChoice, aiChoice)


if __name__ == '__main__':
    for x in range(10):
        userInput = input("Pick Rock(0), Paper(1), Scissors(2): ")
        userChoice = int(userInput)
        print("User chose " + intToHandChoice(userChoice))
        roundResult = playRound(userChoice)
        roundResultStr = intToRoundResult(roundResult)
        print("Round result: " + roundResultStr)
