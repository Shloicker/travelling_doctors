def cost(S, D):
    # This function should take a solution S and the distance matrix D
    # and return its (float) cost. You will need to input your code here. 
    # You are welcome to include other parameters if needed
    return 0.0


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

# The next stage is to produce a solution S and evaluate it via a cost function
S = [[] for i in range(n1)]

# The following lines are for testing purposes and can be deleted
print("n1      = " + str(n1))
print("n2      = " + str(n2))
print("m       = " + str(m))
print("coords  = " + str(coords))
print("D       = " + str(D))
print("S       = " + str(S))
print("cost(S) = " + str(cost(S, D)))