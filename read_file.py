


def display_contents_to_screen(content_to_display):
    print(content_to_display)

def get_file_content(file_spec):
    # Open the file
    my_file_handle = open(file_spec, "r")
    contents_of_file = my_file_handle.read()
    return contents_of_file

# Start program at main
def main():
    """ This is the program driver function """
    # Get File Contents
    file_spec = "CSC_Assignment2_1_Discussion.txt"
    raw_data_from_file = get_file_content(file_spec)
    # Display file contents on the screen
    display_contents_to_screen(raw_data_from_file)

if __name__ -- " __main__ ":
    main()