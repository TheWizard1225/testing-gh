import fcopy as f

# this is the source file where the fcopy function will copy data from
source = "/Users/daniel/Desktop/ProgrammingStuff/PythonStuff/testing-gh/data/input1.txt"

# this is the output file where the fcopy function will write the copied data to
output = "/Users/daniel/Desktop/ProgrammingStuff/PythonStuff/testing-gh/data/output1.txt"

# running the function
f.fcopy(source, output)


# Compares every line from the source file to the output file and checks if they're the same
def testing(original, copy):
    with open(copy, 'rt') as new_file, open(original, 'rt') as old_file:

        if len(new_file.readlines()) != len(old_file.readlines()):
            return False

        for line_number in range(len(new_file.readlines())):
            if new_file.readlines()[line_number] != old_file.readlines()[line_number]:
                return False

    return True


# prints the results from running the test
print("When the fcopy function is run, the result is:")
print(str(testing(source, output)))
