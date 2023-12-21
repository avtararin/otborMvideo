class Pyramid:
    def __init__(self, input_string):
        self.matrix = self.parse_input(input_string)
        self.pyramid = self.fill_triangle(self.matrix, input_string)
        self.matrix_rows = self.count_matrix_size(len(input_string)) + 1
        self.matrix_cols = self.count_matrix_size(len(input_string)) * 2 + 1

    def fill_triangle(self, matrix, string):
        matrix = self.parse_input(string)
        counter = 1
        length = len(string)
        col_trian_last_row = self.count_matrix_size(length)
        rows = col_trian_last_row + 1
        cols = col_trian_last_row * 2 + 1
        index_of_string = 0

        for i in range(rows - 1, -1, -1):
            if (rows - i - 1) % 2 == 0:
                for j in range(cols - (rows - i), rows - 2 - i, -1):
                    matrix[i][j] = string[index_of_string]
                    index_of_string += 1
            else:
                if (i == 0):
                    counter += 1
                for j in range(rows - i - 1, cols - rows + i + 1):
                    matrix[i][j] = string[index_of_string]
                    index_of_string += 1
                counter += 1
        return matrix
    def parse_input(self, string):
        counter = 1
        length = len(string)
        col_trian_last_row = self.count_matrix_size(length)
        rows = col_trian_last_row + 1
        cols = col_trian_last_row * 2 + 1
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        index_of_string = 0

        for i in range(rows - 1, -1, -1):
            if (rows - i - 1) % 2 == 0:
                for j in range(cols - (rows - i), rows - 2 - i, -1):
                    matrix[i][j] = string[index_of_string]
                    index_of_string += 1
            else:
                if (i == 0):
                    counter += 1
                for j in range(rows - i - 1, cols - rows + i + 1):
                    matrix[i][j] = string[index_of_string]
                    index_of_string += 1
                counter += 1
        return matrix

    def count_matrix_size(self, len):
        count_triangle = len // 4
        summ = 0
        nechet = 1
        while (summ != count_triangle):
            summ = summ + nechet
            nechet = nechet + 2
        nechet = nechet - 2
        if len == 1:
            nechet = 1
        return nechet
    def compress(self):
        while len(self.pyramid) > 1:
            self.pyramid = self.compress_pyramid(self.pyramid)

    def compress_pyramid(self, pyramid):
        size = len(pyramid)
        compressed_pyramid = []

        for i in range(0, size, 4):
            for j in range(0, size, 4):
                quad = [
                    pyramid[i][j], pyramid[i][j + 1],
                    pyramid[i + 1][j], pyramid[i + 1][j + 1]
                ]

                if all(elem == quad[0] for elem in quad):
                    compressed_pyramid.append([quad[0]])
                else:
                    compressed_pyramid.append(quad)

        return compressed_pyramid

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.pyramid])


def main():
    with open('input.txt', 'r') as file:
        input_string = file.read()

    pyramid = Pyramid(input_string)
    pyramid.compress()

    with open('output.txt', 'w') as file:
        file.write(str(pyramid))


if __name__ == "__main__":
    main()
