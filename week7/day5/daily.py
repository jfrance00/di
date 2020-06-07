#take bin value of number, reverse it and get the new number represented by new binary value

def input_number():
    number = int(input("Enter a number: "))
    return number

def get_binary(number):
    first_num_bin = '{:032b}'.format(number)
    return first_num_bin

def reverse_bin(bin_number):
    bin_number = str(bin_number)
    reverse_bin = ''
    for digit in bin_number:
        reverse_bin = digit + reverse_bin
    return reverse_bin

def main():
    first_number = input_number()
    binary = get_binary(first_number)
    print("binary: ", binary)
    reversed_binary = reverse_bin(binary)
    print("reversed binary: ", reversed_binary)
    reversed_number = int(reversed_binary,2)
    print("reversed number: ", reversed_number)


    # print(first_num_bin)
    # print(reversed(first_num_bin))
    # print(first_num_bin)

main()