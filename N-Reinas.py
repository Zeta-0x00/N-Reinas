import time
def UbiqueQueen(table, step):
    IndividualStart = time.time()
    for i in range(0, len(table)):
        if (isValid(table, i, step)):
            table[i][step] = 'Z'
            if (step < len(table)-1):
                UbiqueQueen(table, step + 1)
            else:
                printMatrix(table)
                print("------------------  %s"%(time.time()-IndividualStart))
                IndividualStart = time.time()
            table[i][step] = " "

def isValid(table, i, step):
    for x in range(0, step):
        if (table[i][x] == "Z"):
            return False
    j = 0
    while (j < len(table) and (i-j) >= 0 and (step - j) >= 0 ):
        if (table[i-j][step-j] == "Z"):
            return False
        j += 1
    j = 0
    while (j < len(table) and (i + j) < len(table) and (step - j) >= 0):
        if (table[i+j][step-j] == "Z"):
            return False
        j += 1
    return True


def TableGenerator(size):
    table = []
    for i in range(0, size):
        table.append([" "] * size)
    return table


def printMatrix(table):
    STR = ""
    for i in range(len(table)):
        for j in range(len(table[i])):
            STR += table[i][j] + ","
        STR += '\n'
    print(STR)
def GetInt():
    try:
        n = int(input("Ingrese la cantidad de N\n>>>> "))
        return n
    except:
        print("Data Error")
        return GetInt()
table = []
ward = True
size = 4
if __name__ == "__main__":
    size = GetInt()
    table = TableGenerator(size)
    totalStart = time.time()
    UbiqueQueen(table, 0)
    Final = time.time()
    print("Tiempo total de resolcución es %s"%(Final-totalStart))