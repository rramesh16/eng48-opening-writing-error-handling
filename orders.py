
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

# Closing the file automatically
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

# Appending the txt file
def open_and_write_txt(file, item):
    try:
        with open(file, 'a') as file_to_write:
            file_to_write.write(item + '\n')

    except FileNotFoundError as error:
        print('Check your file and the path')
        print(error)
    finally:
        print('////execution done!////')

open_and_write_txt('order2.txt', 'cupcake')
open_and_write_txt('order2.txt', 'OJ with carrots')
open_and_write_txt('order2.txt', 'Benedict Beans')
open_and_write_txt('order2.txt', 'Beans on toast' )

# open_print_txt_file '
# open_print_txt_file('order2.txt')
open_print_close('order2.txt')

