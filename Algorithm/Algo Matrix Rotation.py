# Python 3 solution of the problem:
# https://www.hackerrank.com/challenges/matrix-rotation-algo

def rotate_matrix(mat, m, n, r):
    """Rotation of matrix m rows and n columns
    r time(s) rotation"""
    if r <= 0:
        return mat

    # Number of sub-matrix
    sub = min(m, n) % 2 + int(min(m, n) / 2)

    # For each sub-matrix
    for i in range(sub):
        # Rotate extremity of sub-matrix
        # Size of sub-matrix is (m-2*i) x (n-2*i)
        p = get_perimeter_size(m - 2 * i, n - 2 * i)
        # effective rotation
        er = r % p

        if er == 0:
            pass
        else:
            for j in range(pgcd(p, er)):
                for k in range(int(p / pgcd(p, er)) - 1):
                    c1 = get_cursor_position(m - 2 * i, n - 2 * i, er * k + j, i, True)
                    c2 = get_cursor_position(m - 2 * i, n - 2 * i, er * (k + 1) + j, i, True)
                    # Swap positions
                    mat[c1[0]][c1[1]], mat[c2[0]][c2[1]] = mat[c2[0]][c2[1]], mat[c1[0]][c1[1]]
    return mat

def get_cursor_position(m, n, r, sub, clockwise=False):
    """Returns the r rotations position of the item (0, 0)
    """
    p = get_perimeter_size(m, n)
    r = r % p
    if r == 0:
        i = 0
        j = 0
    # Clockwise rotation
    elif clockwise:
        if r <= (m - 1) + (n - 1) - 1:
            j = min(r, n - 1)
            i = max(r - j, 0)
        elif p - r <= (m - 1):
            i = p - r
            j = 0
        else:
            i = m - 1
            j = p - (m - 1) - r
    # Anti-Clockwise rotation
    else:
        if r <= (m - 1) + (n - 1) - 1:
            i = min(r, m - 1)
            j = max(r - i, 0)
        elif p - r <= (n - 1):
            i = 0
            j = p - r
        else:
            i = p - (n - 1) - r
            j = n - 1
    return i + sub, j + sub

def pgcd(a , b):
    while a % b != 0:
        a, b = b, a % b
    return b

def get_perimeter_size(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return m * n
    else:
        return 2 * (m + n -2)

def print_matrix(mat):
    for r in mat:
        print(' '.join(map(str, r)))

m, n, r = tuple(map(int, input().split(' ')))
mat = []
for row in range(m):
    mat.append(list(map(int, input().split(' '))))
# Run
print_matrix(rotate_matrix(mat, m, n, r))
