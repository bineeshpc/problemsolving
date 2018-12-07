import six

class Number:
    def __init__(self, number):
        
        if number < 0:
            self.sign = 1
            self.number = -number
        else:
            self.sign = 0
            self.number = number

    def get_base_n(self, number, base):
        """
            16 / 2 = 8 0
            8 / 2 = 4 0
            4 / 2 = 2 0
            2 / 2 = 1 0
            1 / 2 = 0 1
            binary of 16 = binary of 16 / 2 followed by 16 % 2
        """
        smaller_number = number / base
        remainder = number % base
        if smaller_number == 0:
            return str(remainder)
        return self.get_base_n(smaller_number, base) + str(remainder)
    
    def get_binary(self):
        if self.sign == 1:
            value = '-0b{}'.format(self.get_base_n(self.number, 2))
        else:
            value = '0b{}'.format(self.get_base_n(self.number, 2))
        return value

    
    def get_octal(self):
        if self.sign == 1:
            value = '-0b{}'.format(self.get_base_n(self.number, 8))
        else:
            value = '0b{}'.format(self.get_base_n(self.number, 8))
        return value

    def get_hexa(self):
        representation = {i: str(i) for i in range(10)}
        for i in range(10, 17):
            representation[i] = chr((i - 10) + ord('A'))
        def get_hexa_helper(n):
            smaller_number = n / 16
            remainder = n % 16
            if smaller_number == 0:
                return representation[remainder]
            else:
                return get_hexa_helper(smaller_number) + representation[remainder]
        if self.sign == 1:
            value = '-0x{}'.format(get_hexa_helper(self.number))
        else:
            value = '0x{}'.format(get_hexa_helper(self.number))
        return value

    def get_number(self):
        if self.sign == 1:
            return -self.number
        else:
            return self.number

    def get_binary_padded(self, n):
        s = self.get_binary()
        length = len(s)
        if length < n:
            if self.sign == 1:
                value = '-0b{}{}'.format((n-length+3) * '0', s[3:])
            else:
                value = '0b{}{}'.format((n-length+2) * '0', s[2:])
        else:
            value = s
        return value

    def get_bit(self, number, i):
        if (number & (1 << i)) > 0:
            return 1
        else:
            return 0

    def get_bits(self):
        if self.sign == 1:
            number = -self.number
        else:
            number = self.number

        length = number.bit_length()
        bits = []
        for i in range(length, -1, -1):
            bits.append(str(self.get_bit(number, i)))
        return ''.join(bits)


class BitwiseOperators:

    @staticmethod
    def or1(a, b):
        return a | b

    @staticmethod
    def and1(a, b):
        return a & b

    @staticmethod
    def xor(a, b):
        return a ^ b

    @staticmethod
    def not1(a):
        """
        ~a only works with signed numbers
        """
        
        return ~a

    @staticmethod
    def leftshift(a, n):
        return a << n

    @staticmethod
    def rightshift(a, n):
        return a >> n


def view_numbers_in_different_bases(n):
    for i in range(n):
        number = Number(i)
        six.print_(i, bw.get_binary(), bw.get_octal(), bw.get_hexa())

def test_operators(a, b, n, func):
    na = Number(a)
    nb = Number(b)
    six.print_(na.get_binary_padded(n))
    six.print_(nb.get_binary_padded(n))
    six.print_(Number(func(a, b)).get_binary_padded(n))
    six.print_()



def main():
    a = 12
    b = a - 1
    n = 8
    test_operators(a, b, n, BitwiseOperators.or1)
    test_operators(a, b, n, BitwiseOperators.and1)
    test_operators(a, b, n, BitwiseOperators.xor)

    six.print_(Number(BitwiseOperators.not1(b)).get_binary_padded(n))
    six.print_(Number(a & BitwiseOperators.not1(b)).get_binary_padded(n))
    six.print_(b)
    six.print_(Number(b).get_bits())
    c = BitwiseOperators.not1(b)
    six.print_(c)
    six.print_(Number(c).get_bits())
    
if __name__ == '__main__':
    main()  