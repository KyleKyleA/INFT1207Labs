# Region function
class find_minimum(object):
    #region function
    def find_minimum(self, user_input):
        """Takes a space seperated string of numbers, returns the smallest value"""
        valid_numbers = []

        #empty number list
        if not user_input:
            raise ValueError("No valid numbers entered. ")

        #Intializing variable
        smallest = user_input[0]
        #Iterates through this for loop and prints if smallest number invalid
        for num in user_input[1:]:
            if  type(num) == int :
                if num < smallest:
                    smallest = num
            else:
                raise ValueError("Smallest number invalid ")
        return smallest
    #endregion function

if __name__ == '__main__':
    min = find_minimum()
