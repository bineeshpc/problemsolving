import six
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

def generate_pascals_triangle_1(n):

    def generate_level(n):
        """
        Simple implementation of pascals triangle
        """
        # base case
        if n == 0:
            generated_values = [1]
        # recursive case
        else:
            generated_values = []
            values = generate_level(n - 1)
            first = 0
            second = 1

            # copy the first element
            # always 1
            generated_values.append(values[first])

            while second:
                try:
                    first_value = values[first]
                    second_value = values[second]
                    generated_values.append(first_value + second_value)
                    first += 1
                    second += 1
                except IndexError:
                    # we reached the end of n - 1 the level
                    # we copy the last element(always 1)
                    # and exit from loop
                    length = second
                    generated_values.append(values[length - 1])
                    second = None
        six.print_(generated_values)
        return generated_values
    generate_level(n)

def generate_pascals_triangle(n):
    def generate_level(n):
        # base case
        if n == 0:
            generated_values = [1]
        # recursive case
        else:
            generated_values = []
            values = generate_level(n - 1)
            even = ((len(values) % 2) == 0)
            length = len(values) // 2
            generated_values.append(values[0])
            for i in range(1, length + 1):
                generated_values.append(values[i-1] + values[i])
            
            if even:
                # copy length - 2 to 0
                # leave the last element alone
                # create an exact mirror image of the rest of the element on RHS
                for i in range(len(generated_values) - 2, -1, -1):
                    generated_values.append(generated_values[i])

            else:
                # copy length - 1 to 0
                # create an exact mirror image of generated values upto now on the RHS
                for i in range(len(generated_values) - 1, -1, -1):
                    generated_values.append(generated_values[i])
        six.print_(generated_values)
        return generated_values


    generate_level(n)


generate_pascals_triangle(10)
