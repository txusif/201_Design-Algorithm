# Matrix Addition
# Matrix 'x' 3x3
x = [[2, 3, 1],
     [2, 4, 4],
     [1, 2, 3]]

# Matrix 'y' 3x3
y = [[3, 2, 4],
     [3, 1, 1],
     [4, 3, 2]]

# Result Matrix 3x4
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result [i][j] = x[i][j] + y[i][j]

print("Matrix 'x'")
for n in x:
    print(n)

print(" ")
print("Matrix 'y'")
for n in y:
    print(n)

print(" ")
print("Addition of Matrix 'x' and Matrix 'y'")
for r in result:
    print(r)