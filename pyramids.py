class Pyramid:
    def __init__(self, input_string):
        self.pyramid = self.fill_triangle(input_string)
        self.matrix_rows = self.count_matrix_size(len(input_string)) + 1
        self.matrix_cols = self.count_matrix_size(len(input_string)) * 2 + 1
        self.string = input_string

    def fill_triangle(self, string):
        self.matrix = self.parse_input(string)
        counter = 1
        length = len(string)
        col_trian_last_row = self.count_matrix_size(length)
        rows = col_trian_last_row + 1
        cols = col_trian_last_row * 2 + 1
        index_of_string = 0

        for i in range(rows - 1, -1, -1):
            if (rows - i - 1) % 2 == 0:
                for j in range(cols - (rows - i), rows - 2 - i, -1):
                    self.matrix[i][j] = string[index_of_string]
                    index_of_string += 1
            else:
                if (i == 0):
                    counter += 1
                for j in range(rows - i - 1, cols - rows + i + 1):
                    self.matrix[i][j] = string[index_of_string]
                    index_of_string += 1
                counter += 1
    def parse_input(self, string):
        counter = 1
        length = len(string)
        if length == 1:
            return self.matrix
        else:
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
        while 1:
            new_string = self.compress_pyramid(self.matrix);
            if len(self.string) == len(new_string):
                break
            else:
                self.string = new_string
                self.matrix = self.parse_input(new_string)
                self.matrix_rows = self.count_matrix_size(len(self.string)) + 1
                self.matrix_cols = self.count_matrix_size(len(self.string)) * 2 + 1

    def compress_pyramid(self, pyramid):
        answer_string = ''
        number_of_lines = 1
        for i in range(1, self.matrix_rows, 2):
            counter_of_pyramids = 0
            number_of_lines += 1
            if (number_of_lines % 2 == 0):
                for j in range(self.matrix_cols - 1, 0, -1):
                    if pyramid[i][j] == 0:
                        continue
                    else:
                        if counter_of_pyramids % 2 == 0:
                            if (pyramid[i][j] == pyramid[i - 1][j - 1] and pyramid[i][j] == pyramid[i][j - 1] and
                                    pyramid[i][j] == pyramid[i][j - 2]):
                                answer_string += str(pyramid[i][j])
                                j -= 3
                                counter_of_pyramids += 1
                        else:
                            if (pyramid[i][j] == pyramid[i - 1][j] and pyramid[i][j] == pyramid[i - 1][j + 1] and
                                    pyramid[i][j] == pyramid[i - 1][j - 1]):
                                answer_string += str(pyramid[i][j])
                                j -= 1
                                counter_of_pyramids += 1
            else:
                for j in range(self.matrix_cols - 1):
                    if pyramid[i][j] == 0:
                        continue
                    else:
                        if counter_of_pyramids % 2 == 0:
                            if (pyramid[i][j] == pyramid[i - 1][j + 1] and pyramid[i][j] == pyramid[i][j + 1] and
                                    pyramid[i][j] == pyramid[i][j + 2]):
                                answer_string += str(pyramid[i][j])
                                j += 3
                                counter_of_pyramids += 1
                        else:
                            if (pyramid[i][j] == pyramid[i - 1][j] and pyramid[i][j] == pyramid[i - 1][j + 1] and
                                    pyramid[i][j] == pyramid[i - 1][j - 1]):
                                answer_string += str(pyramid[i][j])
                                j += 1
                                counter_of_pyramids += 1

        return answer_string


def main():
    with open('input.txt', 'r') as file:
        input_string = file.read()
    pyramid = Pyramid(input_string)
    pyramid.compress()

    with open('output.txt', 'w') as file:
        file.write(str(pyramid.string))


if __name__ == "__main__":
    main()
