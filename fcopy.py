
"""
The fcopy function takes in a file path, reads everything in it,
and pastes all of it into another file based on its path

@:param input_file: File Path
@:param output_file: File Path
@:returns: creates a new file
@:raise FileNotFound: if input_file doesn't exist

"""
def fcopy(input_file, output_file):
    original_string = ""

    with open(input_file, "rt") as original_file:
        for line in original_file:
            original_string += line

    with open(output_file, "wt") as new_file:
        new_file.write(original_string)
