
X = [[]]
O = [[5, 6, 9, 10]]
I = [[1, 5, 9, 13], [4, 5, 6, 7]]
S = [[6, 5, 9, 8], [5, 9, 10, 14]]
Z = [[4, 5, 9, 10], [2, 5, 6, 9]]
L = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
J = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
T = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]

def display(arrays):

    if len(arrays) >= 2:
        arrays.append(arrays[1])

    for array in arrays:
        print()
        for i in range(0, 16):
            print("0" if i in array else "-", "", sep=" ", end="")
            print("\n" if (i + 1) % 4 == 0 else "", end="")

def main():
    switcher = {
        "T": T,
        "J": J,
        "L": L,
        "O": O,
        "I": I,
        "S": S,
        "Z": Z
    }
    array = switcher.get(input(), [])
    display(X + array * (4 // len(array)))


if __name__ == "__main__":
    main()
