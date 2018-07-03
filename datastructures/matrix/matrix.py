
class IncompatibleMatrix(Exception):
    def __init__(self, a_columns, b_rows):
        self.a_columns = a_columns
        self.b_rows = b_rows

    def __str__(self):
        message = []
        message.append('\nMatrices are incompatible.\n')
        message.append('columns of first matrix is not the same as rows of the second matrix \n')
        message.append('number of columns of first matrix = {}\n'.format(self.a_columns))
        message.append('number of rows of second matrix = {}\n'.format(self.b_rows))
        return ''.join(message)

class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        self.initialize(data)
        
    def initialize(self, data=None):
        if data:
            self.data = data
        else:
            self.data = []
            for i in range(self.rows):
                row_i = []
                for j in range(self.columns):
                    row_i.append(0)
                self.data.append(row_i)
        
    def print_matrix(self):
        for i in range(self.rows):
            print
            for j in range(self.columns):
                print self.data[i][j],


    def __mul__(self, other):
        if self.columns != other.rows:
            raise IncompatibleMatrix(self.columns, other.rows)
        else:
            c = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    c.data[i][j] = 0
                    for k in range(self.columns): # or other.rows
                        c.data[i][j] += self.data[i][k] * other.data[k][j]
            return c


if __name__ == '__main__':
    a = [[1, 2, 3],
         [3, 4, 5]
         ]


    b = [[1, 2],
         [3, 4],
         [6, 7]
        ]


    a = Matrix(2, 3, a)
    b = Matrix(3, 2, b)
    a.print_matrix()
    b.print_matrix()

    c = a * b

    c.print_matrix()
    
    b_incompatible = Matrix(2, 2, [[1, 2], [1, 2]])

    c = a * b_incompatible

    
    
