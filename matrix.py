from superArray import SuperArray


# Matrix data structure: You can create a matrix with any number of rows and columns,
# it unnecessarily uses the SuperArray to create each row.
class SuperMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [SuperArray(0, cols-1) for _ in range(rows)]

    def set(self, row, col, val):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError(f"Invalid index value. This matrix has {self.rows} rows and {self.cols} columns.")
        self.matrix[row].set(col, val)

    def get(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError(f"Invalid index value. This matrix has {self.rows} rows and {self.cols} columns.")
        return self.matrix[row].get(col)

    def print(self):
        for sa in self.matrix:
            sa.print()


# Matrix data structure: You can create a matrix with any number of rows and columns.
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[None]*cols for _ in range(rows)]

    def set(self, row, col, val):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError(f"Invalid index value. This matrix has {self.rows} rows and {self.cols} columns.")
        self.matrix[row][col] = val

    def get(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError(f"Invalid index value. This matrix has {self.rows} rows and {self.cols} columns.")
        return self.matrix[row][col]

    def print(self):
        print(self.matrix)

