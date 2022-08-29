
O = [[4, 14, 15, 5]]
I = [[4, 14, 24, 34], [3, 4, 5, 6]]
S = [[5, 4, 14, 13], [4, 14, 15, 25]]
Z = [[4, 5, 15, 16], [5, 15, 14, 24]]
L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]

class Array:

    def __init__(self, data, cols, rows):
        self.index = 0
        self.data = data
        self.cols = cols
        self.rows = rows
        self.size = cols * rows

    def display(self, show):
        print()
        for i in range(0, self.size):
            print("0" if show and i in self.data[self.index] else "-", "", sep=" ", end="")
            print("\n" if (i + 1) % self.cols == 0 else "", end="")

    def down(self):
        for piece in self.data:
            for i in range(len(piece)):
                piece[i] = (piece[i] + self.cols) % self.size

    def rotate(self):
        self.index = (self.index + 1) % len(self.data)
        self.down()




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

    piece = switcher.get(input(), [[]])
    while True:
        try:
            dimenssions = input().split(" ")
            cols = int(dimenssions[0])
            rows = int(dimenssions[1])
            break
        except Exception as e:
            print(e)

    array = Array(piece, cols, rows)
    array.display(False)
    array.display(True)

    while True:
        instruction = input()
        if instruction == "exit":
            break
        elif instruction == "rotate":
            array.rotate()
        # elif instruction == "left":
        #     left(array)
        # elif instruction == "righ":
        #     right(array)
        elif instruction == "down":
            array.down()
        # else:
        #     pass
        array.display(True)

if __name__ == "__main__":
    main()
