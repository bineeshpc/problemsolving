"""
Pascals triangle

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1


"""


def generate_pascals_triangle(n):
    def generate_level(n):
        # base case
        generated_values = []
        if n == 0:
            generated_values = [1]
        # recursive case
        else:
            values = generate_level(n - 1)
            first = 0
            second = 1
            
            generated_values.append(values[first])

            while second:
                try:
                    first_value = values[first]
                    second_value = values[second]
                    generated_values.append(first_value + second_value)
                    first += 1
                    second += 1
                except IndexError:
                    length = second
                    generated_values.append(values[length - 1])
                    second = None
        print generated_values
        return generated_values


    generate_level(n)


generate_pascals_triangle(10)
