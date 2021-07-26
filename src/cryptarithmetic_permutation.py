import time


def findIndex(elmt, list):
    i = 0
    found = False
    while (i < len(list) and not(found)):
        if(list[i] == elmt):
            found = True
        i += 1

    if(not(found)):
        return -1
    else:
        return i-1


def readFile(fileName):
    f_input = open(fileName, "r")
    words_input = f_input.read().splitlines()
    f_input.close()
    return words_input


def makeAlphabetList(wordList):
    alphabetList = ""
    for words in wordList:
        if(words[0] == '-'):
            continue
        else:
            for alphabet in words:
                if((findIndex(alphabet, alphabetList) != -1)):
                    continue
                else:
                    alphabetList += alphabet

    return alphabetList


def isAnswer(wordList, alphabetList, numList):
    ans = 0
    num = ""

    if(numList[0] == 0):
        return False

    # Calculating operands
    for words in wordList:
        if(words[0] == '-'):
            break
        else:
            num = ""
            for alphabet in words:
                if(findIndex(alphabet, alphabetList) == -1):
                    continue
                else:
                    num += str(numList[findIndex(alphabet, alphabetList)])
            ans += int(num)

    # Check if equation is true
    num = ""
    for alphabet in wordList[-1]:
        num += str(numList[findIndex(alphabet, alphabetList)])
        if(num[0] == '0'):
            return False

    return int(num) == ans


def printAnswer(wordList, alphabetList, numList):
    blank = 0
    for alphabet in alphabetList:
        print("%s : %d" %
              (alphabet, numList[findIndex(alphabet, alphabetList)]))
    print()

    for words in wordList:
        if(words[0] == '-'):
            continue
        if(len(words) > blank):
            blank = len(words)

    print("SOLUTION :")
    print()

    for words in wordList:
        if(words[0] == '-'):
            print('-'*blank, end="")
            print('+')
        else:
            print(" "*(blank-len(words)), end="")
            print(words)
    print()

    for words in wordList:
        if(words[0] == '-'):
            print('-'*blank, end="")
            print('+')
        else:
            print(" "*(blank-len(words)), end="")
            for i in range(len(words)):
                print(numList[findIndex(words[i], alphabetList)], end="")
            print()
    print()


def nextPermutation(numList):
    ans = [0 for i in range(len(numList))]
    for i in range(len(numList)):
        ans[i] = numList[i]

    i = len(ans) - 1
    while i > 0 and ans[i-1] >= ans[i]:
        i = i - 1
    if i <= 0:
        return []

    j = len(ans) - 1
    while ans[j] <= ans[i - 1]:
        j = j - 1
    ans[i-1], ans[j] = ans[j], ans[i-1]

    ans[i:] = ans[len(ans) - 1: i-1: -1]

    return ans


def cryptBruteForce(wordList, alphabetList):
    numList = [0 for i in range(len(alphabetList))]
    test = 1
    noSolution = False

    for i in range(len(alphabetList)):
        numList[i] = i

    startTime = time.time()
    currPermutation = numList

    while(not(isAnswer(wordList, alphabetList, currPermutation)) and not(noSolution)):
        test += 1
        currPermutation = nextPermutation(currPermutation)

        if(len(currPermutation) == 0):
            if(len(alphabetList) == 10):
                noSolution = True

            else:
                index = len(alphabetList) - 1
                if(numList[index] == 9):
                    while(numList[index] == 10 - len(alphabetList) + index):
                        index -= 1

                    numList[index] += 1

                    if(numList[0] > 10 - len(alphabetList)):
                        noSolution = True

                    index += 1

                    while(index < len(alphabetList)):
                        numList[index] = numList[index-1] + 1
                        index += 1

                else:
                    numList[index] += 1

            currPermutation = numList

    if(noSolution):
        print("NO SOLUTION!!")
        input("Tekan enter untuk menutup program!!")
    else:
        printAnswer(wordList, alphabetList, currPermutation)
        print("Jumlah tes :", test)
        print("Waktu pemrosesan : %s detik" % (time.time() - startTime))
        print()


ongoing = True
while(ongoing):
    fileName = input("Masukkan nama file : ")
    root = "../test/" + fileName
    wordList = readFile(root)
    alphabetList = makeAlphabetList(wordList)
    cryptBruteForce(wordList, alphabetList)

    cmd = input("Apakah anda masih ingin menghitung persamaan lain? (Y/N): ")

    if(cmd == 'Y'):
        ongoing = True
    elif(cmd == 'N'):
        ongoing = False
