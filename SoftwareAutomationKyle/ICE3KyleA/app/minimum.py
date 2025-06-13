# Region function
class find_minimum(object):


    def find_minimum(self):
        """Takes a space seperated string of numbers, returns the smallest value"""
        valid_numbers = []
        items = self.split()

        for item in items:
            try:
                num = int(item)
                valid_numbers.append(num)
            except ValueError:
                pass
        if not valid_numbers:
            raise ValueError("No valid numbers entered. ")

        smallest = valid_numbers[0]
        for num in valid_numbers[1:]:
            if num < smallest:
                smallest = num
        return smallest

if __name__ == '__main__':
    min = find_minimum()
