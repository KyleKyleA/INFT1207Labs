# Region function
class find_minimum(object):

    def find_minimum(self, user_input):
        """Takes a space seperated string of numbers, returns the smallest value"""
        valid_numbers = []

        if not user_input:
            raise ValueError("No valid numbers entered. ")

        smallest = user_input[0]
        for num in user_input[1:]:
            if  type(num) == int :
                if num < smallest:
                    smallest = num
            else:
                raise ValueError("Smallest number invalid ")
        return smallest


if __name__ == '__main__':
    min = find_minimum()
