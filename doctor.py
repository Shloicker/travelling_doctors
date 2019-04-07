import random

# Main Program: First ask the user to specify the input file.
filename = input("Enter problem file name >> ")

# Now read the input file line by line
with open(filename, "r") as f:

    # Read the first line of the file to get values for n1, n2, m (and N)
    line = f.readline().split()
    n1 = int(line[0])
    n2 = int(line[1])
    m = int(line[2])
    N = n1 + n2

    # Now define the arrays to hold the coordinates and the distances
    coords = [[0,0] for i in range(N)]
    D = [[0 for i in range(N)] for i in range(N)]

    # Now read in the coordinates
    for i in range(N):
        line = f.readline().split()
        coords[i][0] = float(line[0])
        coords[i][1] = float(line[1])

    # Finally read in the distance matrix
    for i in range(N):
        line = f.readline().split()
        for j in range(N):
            D[i][j] = float(line[j])

print(filename + " has been read in correctly.")



#TASK 1

def createRoutes(n1, n2, m):

    sol = []
    S = [[] for i in range(n1)]
    patientList = []
    for i in range(n2): 
        patientList.append(i)

    while(len(patientList) > 0):
            rand1 = random.randint(0, len(patientList)-1)
            rand2 = random.randint(0, len(S)-1)
            if len(S[rand2]) == m:
                sol.append(S[rand2])
                S.pop(rand2)
                n1 = n1-1
            else:
                S[rand2].append(patientList[rand1])
                patientList.pop(rand1)

    for i in range (len(sol)):
        S.append(sol[i])
    return S


def cost(S, D, n1):
    price = 0
    for i in range(n1):

        for j in range(0, len(S[i])+1):
            if j == 0:
                price += D[i][S[i][j]+n1]

            elif j>0 and j <= len(S[i])-1: 
                price+= D[n1+S[i][j]][n1+S[i][j-1]]
            else:
                price += D[n1+S[i][j-1]][i]

    return price



solution = createRoutes(n1, n2, m)
sol_cost = cost(solution, D, n1)

print("Randomly generated solution:\n\n" + str(solution) + "\n\nSolution cost:\n" + str(sol_cost))