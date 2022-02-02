# Matrix Multiplication
# Matrix 'x' 3x3
x = [[2, 3, 1],
     [2, 4, 3],
     [1, 2 , 3]]

# Matrix 'y' 3x4
y = [[2, 4, 1, 2],
     [1, 2, 3, 4],
     [5, 3, 2, 1]]

# Result Matrix 3x4
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

print("Matrix 'x'")
for n in x:
    print(n)

print(" ")
print("Matrix 'y'")
for n in y:
    print(n)

print(" ")
print("Multiplication of Matrix 'x' and Matrix 'y'")
for r in result:
    print(r)