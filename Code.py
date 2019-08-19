def num_of_steps(X):
    n = len(X)
    count = 0
    for i in range(n-1):
        if abs(X[i+1][0]-X[i][0]) > abs(X[i+1][1]-X[i+1][0]):
            count += abs(X[i+1][0] - X[i][0])
        else:
            count += abs(X[i+1][1] - X[i][1])
    return count

X = [(0, 0), (1, 1), (1, 2)]
print(num_of_steps(X))
