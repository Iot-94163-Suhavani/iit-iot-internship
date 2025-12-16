
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


B = (
    (10, 20, 30, 40),
    (50, 60, 70, 80),
    (90, 100, 110, 120)
)

def add_sub_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    
    add_result = []
    sub_result = []
    
    for i in range(rows):
        add_row = []
        sub_row = []
        for j in range(cols):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)
    
    return add_result, sub_result


sum_matrix, diff_matrix = add_sub_matrices(A, B)

print("Addition:")
for row in sum_matrix:
    print(row)

print("\nSubtraction:")
for row in diff_matrix:
    print(row)