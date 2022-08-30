import copy

O = [[4, 14, 15, 5]]
I = [[4, 14, 24, 34], [3, 4, 5, 6]]
S = [[5, 4, 14, 13], [4, 14, 15, 25]]
Z = [[4, 5, 15, 16], [5, 15, 14, 24]]
L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]


class StackedPieces:

    def __init__(self, cols, rows):
        self.stacked_pieces = set()
        self.cols = cols
        self.size = cols * rows

    def add(self, piece):
        self.stacked_pieces.update(piece.data[piece.index])

    def in_stack(self, i):
        return i in self.stacked_pieces

    def break_line(self):
        if all(pixel in self.stacked_pieces for pixel in [i for i in range(self.size - self.cols, self.size)]):
            self.stacked_pieces = set(self.stacked_pieces - set(range(self.size - self.cols, self.size)))
            self.stacked_pieces = set([pixel + self.cols for pixel in self.stacked_pieces])
        else:
            print("last line not stacked")

    def display(self):
        print("***Stacked***")
        for i in self.stacked_pieces:
            print(i, "", sep=" ", end="")
        print()

class Piece:

    def __init__(self, data, cols, rows, stack):
        self.index = 0
        self.data = data
        self.cols = cols
        self.rows = rows
        self.size = cols * rows
        self.stack = stack
        self.floor = False
        self.stacked = False


    def check_floor(self):
        for i in self.data[self.index]:
            if i >= self.size - self.cols:
                self.floor = True

    def down(self):
        if not self.stacked:
            for pixels in self.data:
                for i in range(len(pixels)):
                    pixels[i] = pixels[i] + self.cols
                    if pixels[i] > self.size:
                        pixels[i] %= self.size
            self.check_floor()

    def rotate(self):
        if not self.floor:
            self.index = (self.index + 1) % len(self.data)
        self.check_floor()
        if not self.floor:
            self.down()


    def can_go_left(self, pixels):
        for i in pixels:
            if i % self.cols == 0:
                return False
        return True

    def left(self):
        for pixels in self.data:
            if self.can_go_left(pixels):
                self.move(pixels, -1)
        self.down()

    def can_go_right(self, pixels):
        for i in pixels:
            if i % self.cols == self.cols - 1:
                return False
        return True


    def right(self):
        for pixels in self.data:
            if(self.can_go_right(pixels)):
                self.move(pixels, 1)
        self.down()

    def move(self, pixels, index):
        for i in range(len(pixels)):
            pixels[i] = pixels[i] + index

def display(piece, stack, show):
    print()
    space = False
    for pixel in range(0, piece.size):
        if space:
            print("\t", end="")
        print(pixel if show and (pixel in piece.data[piece.index] or stack.in_stack(pixel)) else "-", end="")
        space = True
        if (pixel + 1) % piece.cols == 0:
            print()
            space = False

def get_dimenssions():
    while True:
        try:
            dimenssions = input().split(" ")
            cols = int(dimenssions[0])
            rows = int(dimenssions[1])
            return cols, rows
        except Exception as e:
            print(e)

def main():
    switcher = {"T": T, "J": J, "L": L, "O": O, "I": I, "S": S, "Z": Z}
    choice = switcher.get(input(), [[]])
    cols, rows = get_dimenssions()
    stack = StackedPieces(cols, rows)
    piece = Piece(copy.deepcopy(choice), cols, rows, stack)
    display(piece, stack, False)
    display(piece, stack, True)

    while True:
        instruction = input()
        if instruction == "exit":
            break
        if piece.floor:
            if not piece.stacked:
                stack.add(piece)
                piece.stacked = True
        if instruction == "piece":
            if not piece.stacked:
                print("previous piece has not been stacked")
            else:
                new_choice = switcher.get(input(), [[]])
                piece = Piece(copy.deepcopy(new_choice), cols, rows, stack)
                print("new piece")
                print(piece.data[piece.index])
        elif instruction == "rotate":
            piece.rotate()
        elif instruction == "left":
            piece.left()
        elif instruction == "right":
            piece.right()
        elif instruction == "break":
            if piece.stacked:
                piece = Piece([[]], cols, rows, stack)
                piece.stacked = True
                stack.break_line()
            else:
                print("Piece not stacked!!!")
        else:
            piece.down()
        display(piece, stack, True)
        stack.display()

if __name__ == "__main__":
    main()
