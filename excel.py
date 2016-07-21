class Cell:
    def __init__(self):
        self.links = []
        self.value = None

    def get_links(self):
        return self.links

    def set_value(self, val):
        self.value = val

    def set_links(self, links):
        self.links += links

    def _get_value(self, root):
        if root is None:
            return 0
        if len(root.get_links()) == 0:
            return root.value
        else:
            sum = 0
            for n in root.get_links():
                if n == root:
                    sum += root.value
                else:
                    sum += self._get_value(n)

        return sum

    def get_value(self):
        if len(self.links):
            return self._get_value(self)

        return self.value

class Document:
    def __init__(self):
        self.x_dim = 10
        self.y_dim = 10
        self.data = [[Cell() for i in xrange(0, self.x_dim)] for j in xrange(0, self.y_dim)]

    def set_x(self, x):
        self.x_dim = x

    def set_y(self, y):
        self.y_dim = y

    def set_cell(self, x, y, val):
        if val is not None:
            self.data[x][y].set_value(val)

    def get_cell_value(self, x, y):
        return self.data[x][y].get_value()

    def import_mtx(self, mtx):
        self.x_dim = len(mtx[0])
        self.y_dim = len(mtx)
        self.data = [[Cell() for i in xrange(0, self.x_dim)] for j in xrange(0, self.y_dim)]
        for row in xrange(len(mtx[0])):
            for col in xrange(0,len(mtx)):
                self.data[row][col].set_value(mtx[row][col])

    def sum_col(self, col):
        sum = 0
        if col < len(self.data[0]):
            for i in xrange(len(self.data)):
                sum += self.data[i][col].get_value()

        return sum

    def print_data(self):
        print
        for i in xrange(0, len(self.data)):
            row_str = ''
            for j in xrange(0, len(self.data[0])):
                row_str += str(self.data[i][j].get_value()) + ' '
            print row_str

    def get_cell(self, x, y):
        return self.data[x][y]

    def set_links(self, x, y, links):
        self.data[x][y].set_links(links)

d = Document()
d.set_cell(0, 0, 1)
d.import_mtx([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
d.print_data()
print 'column sum: ' + str(d.sum_col(1))
d.set_links(0, 0, [d.get_cell(0, 0), d.get_cell(1, 1), d.get_cell(2, 2)])
print 'cell (0,0): ' + str(d.get_cell_value(0,0))


