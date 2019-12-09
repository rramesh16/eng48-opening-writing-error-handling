
def open_print_txt_file(file_name):
    try:
        opened_file = open(file_name, 'r')
        lines = opened_file.readlines()
        for line in lines:
            print(line.strip('/n'))

        opened_file.close()      # This closes the file so it can be saved without conflict

    except FileNotFoundError as errmssg:  # the errmssg captures the original error message
        print('Check file name and/or path- File cannot be found ')
        print(errmssg)  # Printing the orignal error message
        # raise   #--> raising the error

def open_print_close(file_name):
    try:
        with open(file_name, 'r') as file:    # With will automatically open and close a file
            lines = file.readlines()
            for line in lines:
                print(line.strip('/n'))

    except FileNotFoundError as error:
        print('Check your file')
        print(error)

    finally:
        print('////execution done!////')


# open_print_txt_file('order.txt')
# open_print_txt_file('order2.txt')
open_print_close('order2.txt')

