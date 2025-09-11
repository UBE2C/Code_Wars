
# ============== #
#    CodeWars    #
# ============== #







###################################################################################################  Grasshopper kata  #####################################################################################################

testArray = [1, 2, 3, 4 ,5, 6]
def find_average (nums):
    average = sum(nums) / len(nums)

    return average

find_average(testArray)

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Position Average kata  #####################################################################################################




## Some test cases and warm up stuff
# Test set 1
s1 = "6900690040"
s2 = "4690606946"
s3 = "9990494604"


# Testing some basic array functionality for the prototypes
test_string = "444996, 699990, 666690, 444996, 444996"

test_piece = range(0,5)

test_string[6:]
len(test_string[0:6])

a = []

a.append(test_string[0:6])
a.append(test_string[8:14])
print(a)
len(a)
len(a[1])

len(test_string)




## Writing sub functions for the main function


# Prototype compare function for the main function, works with 2 strings, but not with more.
def string_position_compare(string1, string2):
    matches = 0
    positions = []

    for index in range(0, len(string1)):
    
        if string1[index] == string2[index]:
            matches = matches + 1
            positions.append(index)
    
    return f"{matches} matches were found in the following positions: {positions}"

string_position_compare(s1, s2)
string_position_compare(s1, s3)
string_position_compare(s2, s3)


# Test set 2
test_string = "444996, 699990, 666690, 444996, 444996"
test_string_2 = "444996, 699990"
test_string_3 = "444996", "699990", "666690", "444996", "444996"
test_string_4 = "6900690040", "4690606946", "9990494604"
test_string_5 = "6900690040, 4690606946, 9990494604"


# Prototype string breaker function for the main functions. works as intended.
def string_breaker(string):
    
    broken_list = []
    next_piece_start = 0

    for chr_index in range(0, len(string)):

        if string[chr_index] == ",":
            broken_list.append(string[next_piece_start:chr_index])
            next_piece_start = chr_index + 2
        
    broken_list.append(string[next_piece_start:])
            
    return broken_list

string_breaker(test_string)
string_breaker(test_string_2)

# Another prototype matching function for the main function. Can handle multiple strings.
# Works as intended
def test_function(string_lst):
    seq_len = len(string_lst[1])
    matches = 0

    for i in range(len(string_lst)):
        example = string_lst[i]
        print(example)
        for e in range(i + 1, len(string_lst)):
            comparison = string_lst[e]
            print(comparison)
            for char in range(0, seq_len):
                if example[char] == comparison[char]:
                    matches = matches + 1

    print(matches)

test_function(test_string_4)


# Test set 3
s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"
s2 = "444996, 699990, 666690, 096904"
s3 = "46099969, 64096999, 44949949, 06409969, 09064604, 90490494, 04600696, 94469969"
s4 = "0, 0, 0, 0, 0, 0, 0, 0"




## Writing and prototyping the main function


# Prototype main function (seems to be working, needs some polish)    
def pos_average(string):
    ## NOTE: Define the "string_breaker" part of the main function
    # Define an empty list and an empty vector for further iteration
    broken_list = []
    next_piece_start = 0

    # This for loop will walk along the un-split list and will look for commas (the separators)
    for chr_index in range(0, len(string)):

        # If a comma is found this if statement will split off the portion before the comma
        # and will set the new piece starting position to the beginning of the next piece
        # The + 2 comes from the comma and from the space after, if the formatting is different
        # like a space is missing this will not work
        if string[chr_index] == ",":
            broken_list.append(string[next_piece_start:chr_index])
            next_piece_start = chr_index + 2

    # This last piece will ensure that the last string after the last comma is also added to the list    
    broken_list.append(string[next_piece_start:])


    ## NOTE: Define the "position_compare" part of the main function
    # Define the character sequence length for each piece to compare as "seq_len" 
    seq_len = len(broken_list[0])
    # Define an empty list and an empty vector for further iteration
    matches_lst = []
    matches = 0
    
    # This is a triple nested for loop. For noobs like me, note that the execution of the loops will go from
    # inside out!
    # This outermost one is responsible for feeding the
    # the "example" string to which the other strings will be compared to
    for i in range(len(broken_list)):
        example = broken_list[i]
        print(example)

        # The second layer loop will be responsible for feeding the "comparison" strings which will be
        # compared to the "example" string
        for e in range(i + 1, len(broken_list)):
            comparison = broken_list[e]
            print(comparison)

            # The innermost loop will be responsible for the movement along the two strings being compared
            # by the if statement found in it 
            for char in range(0, seq_len):

                # The if statement inside the for loop is responsible for doing the character to character comparison
                # and noting down any matches if found
                if example[char] == comparison[char]:
                    matches = matches + 1
                    matches_lst.append(matches)


    ## NOTE: Define the mean calculation part of the main function
    # Define the number of combinations for the comparisons for n character stings:
    # (n * n - 1) / 2        
    n_combinations = (len(broken_list) * (len(broken_list) - 1)) / 2
    # Define the mean score based on the number of total matches, the number of possible 
    # combinations and on the length of the character strings:
    score = (matches / (n_combinations * seq_len)) * 100
    # Define the final rounded score to return
    rounded_score = round(score, 10)
        

    # Return the final score
    return matches, rounded_score
    
pos_average(s4)


# Test set 4
s3 = "46099969, 64096999, 44949949, 06409969, 09064604, 90490494, 04600696, 94469969"
s4 = "0, 0, 0, 0, 0, 0, 0, 0"
s5 = "192423"
s6 = "253614/251436"


# The second, polished prototype
def pos_average(string):
    ## NOTE: Define the "string_breaker" part of the main function
    # Define an empty list and an empty vector to store the desired character strings
    # and to define the starting position of the string about to be split off
    broken_list = []
    next_piece_start = 0

    # This for loop will walk along the un-split list and will look for commas (the separators)
    for chr_index in range(0, len(string)):

        # If a comma is found this if statement will split off the portion before the comma
        # and will set the new piece starting position to the beginning of the next piece
        # The + 2 comes from the comma and from the space after, if the formatting is different
        # like a space is missing this will not work
        if string[chr_index] == ",":
            broken_list.append(string[next_piece_start:chr_index])
            next_piece_start = chr_index + 2

    # This last piece will ensure that the last string after the last comma is also added to the list    
    broken_list.append(string[next_piece_start:])

    ## NOTE: this wrapper if statement will ensure that the function will only be executed if the
    # the right number of substrings are present and if the formatting is correct
    # (e.g: using a comma to separate the substrings)
    if len(broken_list) < 2:
        return f"""Error in pos_average: the supplied character string is either formatted wrong,
                or contains less than two substrings to compare.
                Please check the supplied string:
                {string}"""
    else:
        ## NOTE: Define the "position_compare" part of the main function
        # Define the character sequence length for each piece to compare as "seq_len" 
        seq_len = len(broken_list[0])
        # Define an empty vector for calculating the number of character matches
        matches = 0
    
        # This is a triple nested for loop. For noobs like me, note that the execution of the loops will go from
        # inside out!
        # This outermost one is responsible for feeding the
        # the "example" string to which the other strings will be compared to
        for i in range(len(broken_list)):
            example = broken_list[i]

            # The second layer loop will be responsible for feeding the "comparison" strings which will be
            # compared to the "example" string
            for e in range(i + 1, len(broken_list)):
                comparison = broken_list[e]

                # The innermost loop will be responsible for the movement along the two strings being compared
                # by the if statement found in it 
                for char in range(0, seq_len):

                    # The if statement inside the for loop is responsible for doing the character to character comparison
                    # and noting down any matches if found
                    if example[char] == comparison[char]:
                        matches = matches + 1


        ## NOTE: Define the mean calculation part of the main function
        # Define the number of combinations for the comparisons for n character stings:
        # (n * n - 1) / 2        
        n_combinations = (len(broken_list) * (len(broken_list) - 1)) / 2
        # Define the mean score based on the number of total matches, the number of possible 
        # combinations and on the length of the character strings:
        score = (matches / (n_combinations * seq_len)) * 100
        # Define the final rounded score to return
        rounded_score = round(score, 10)


    # Return the final score
    return rounded_score

pos_average(s6)




## The final, submitted version of the main function
def pos_average(s):
    ## NOTE: Define the "string_breaker" part of the main function
    # Define an empty list and an empty vector to store the desired character strings
    # and to define the starting position of the string about to be split off
    broken_list = []
    next_piece_start = 0

    # This for loop will walk along the un-split list and will look for commas (the separators)
    for chr_index in range(0, len(s)):

        # If a comma is found this if statement will split off the portion before the comma
        # and will set the new piece starting position to the beginning of the next piece
        # The + 2 comes from the comma and from the space after, if the formatting is different
        # like a space is missing this will not work
        if s[chr_index] == ",":
            broken_list.append(s[next_piece_start:chr_index])
            next_piece_start = chr_index + 2

    # This last piece will ensure that the last string after the last comma is also added to the list    
    broken_list.append(s[next_piece_start:])

    ## NOTE: this wrapper if statement will ensure that the function will only be executed if the
    # the right number of substrings are present and if the formatting is correct
    # (e.g: using a comma to separate the substrings)
    if len(broken_list) < 2:
        return f"""Error in pos_average: the supplied character string is either formatted wrong,
                or contains less than two substrings to compare.
                Please check the supplied string:
                {s}"""
    else:
        ## NOTE: Define the "position_compare" part of the main function
        # Define the character sequence length for each piece to compare as "seq_len" 
        seq_len = len(broken_list[0])
        # Define an empty vector for calculating the number of character matches
        matches = 0
    
        # This is a triple nested for loop. For noobs like me, note that the execution of the loops will go from
        # inside out!
        # This outermost one is responsible for feeding the
        # the "example" string to which the other strings will be compared to
        for i in range(len(broken_list)):
            example = broken_list[i]

            # The second layer loop will be responsible for feeding the "comparison" strings which will be
            # compared to the "example" string
            for e in range(i + 1, len(broken_list)):
                comparison = broken_list[e]

                # The innermost loop will be responsible for the movement along the two strings being compared
                # by the if statement found in it 
                for char in range(0, seq_len):

                    # The if statement inside the for loop is responsible for doing the character to character comparison
                    # and noting down any matches if found
                    if example[char] == comparison[char]:
                        matches = matches + 1


        ## NOTE: Define the mean calculation part of the main function
        # Define the number of combinations for the comparisons for n character stings:
        # (n * n - 1) / 2        
        n_combinations = (len(broken_list) * (len(broken_list) - 1)) / 2
        # Define the mean score based on the number of total matches, the number of possible 
        # combinations and on the length of the character strings:
        score = (matches / (n_combinations * seq_len)) * 100
        # Define the final rounded score to return
        rounded_score = round(score, 10)


    # Return the final score
    return rounded_score

pos_average(s6)

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Convert a Number  #####################################################################################################
                                                                                                  #     to a String!   #

def number_to_string(num):
    converted = str(num)
    return converted

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Highest Rank Number  #####################################################################################################
                                                                                                  #     in an Array       #




## A more rudimentary solution built on loops


# Character recognition loop prototype 1
input_array = [12, 10, 8, 12, 7, 6, 4, 10, 12]

element_count_list = [[1] for i in range(len(input_array))]

search_array = input_array.copy()

for i in range(len(input_array)):
    example_element = input_array[i]
    print(i)
    times_element_present = 1
    

    for index_2 in range(i + 1, len(input_array)):
        compare_element = input_array[index_2]
        print(index_2)
        
        if input_array[i] == input_array[index_2]:
            times_element_present = times_element_present + 1

        
        element_count_list[i] = times_element_present

print(element_count_list)


# Character recognition loop prototype 2 (dynamically decreasing search array)
input_array = [12, 10, 8, 12, 7, 6, 4, 10, 10]
count_lst = []
search_array = input_array.copy()

for i in range(len(input_array)):
    times = 0
    for e in range(len(search_array)):
        if input_array[i] == search_array[e]:
            times = times + 1
        #element_count_list[i] = times
    count_lst.append(times)
    for item in search_array:
        if item == input_array[i]:
            search_array.remove(item)
print(count_lst)


# Highest rank return
match_lst = []

if count_lst.count(max(count_lst)) == 1:
    print(input_array[count_lst.index(max(count_lst))])
else:
    for index in range(len(count_lst)):
        if count_lst[index] == max(count_lst):
            match_lst.append(input_array[index])
print(max(match_lst))


## Putting together the prototype function
def highest_rank(arr):
    # Define a list which will store the count for the repeated elements
    count_lst = []

    # Create a search array which can be dynamically sized
    search_array = arr.copy()

    # This nested loop will do the following: 
    # First and second loop: count the number of repeats for each element
    # Third loop: will remove the already noted elements form the search list
    # so they are not counted again
    for i in range(len(arr)):
        times = 0
        for e in range(len(search_array)):
            if arr[i] == search_array[e]:
                times = times + 1
        count_lst.append(times)
        for item in search_array:
            if item == arr[i]:
                search_array.remove(item)

    # Create a list to store potentially matched values
    match_lst = []

    # This if statement will decide if the highest ranking element is matched with other
    # elements or not. If yes, it will return the greatest highest ranking element.
    if count_lst.count(max(count_lst)) == 1:
        return arr[count_lst.index(max(count_lst))]
    else:
        for index in range(len(count_lst)):
            if count_lst[index] == max(count_lst):
                match_lst.append(arr[index])
    return max(match_lst)


test_array_1 = [12, 10, 8, 12, 7, 6, 4, 10, 12]              
test_array_2 = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          
test_array_3 = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]
test_array_4 = [12, 10, 8, 12, 7, 6, 4, 10, 10]
test_array_5 = [1, 2, 3]

highest_rank(test_array_1)
highest_rank(test_array_2)
highest_rank(test_array_3)
highest_rank(test_array_4)
highest_rank(test_array_5)

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Leap year  #####################################################################################################
                                                                                                  #             #




## Testing some basic functions and principles
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True

    else:
        return False

is_leap_year(year = 1600)

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  alternate  #####################################################################################################
                                                                                                  #   6 kyu     #


"""Write a function that determines if a word has alternating consonants and vowels and returns True or False accordingly"""
def alternate(word: str) -> bool:
    vowels: set[str] = {"a", "e", "i", "o", "u"}
    answer: bool = bool()


    for i in range(len(word) - 1):
        if word[i] in vowels and word[i+1] not in vowels:
            answer = True
        elif word[i] not in vowels and word[i+1] in vowels:
            answer = True
        else:
            answer = False
            break

    return answer

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  HQ9+ interpreter  #####################################################################################################
                                                                                                  #       8 kyu        #

"""You task is to implement an simple interpreter for the notorious esoteric language HQ9+ that will work for a single character input:

If the input is 'H', return 'Hello World!'
If the input is 'Q', return the input
If the input is '9', return the full lyrics of 99 Bottles of Beer."""
def HQ9_interpreter(character: str) -> str:
    #Initialize the output
    output_str: str = ""

    #Input check
    if character == "H":
        output_str = "Hello World!"
    elif character == "Q":
        output_str = character
    elif character == "9":
        for i in range (99, -1, -1):
            if i > 2:
                output_str += f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i - 1} bottles of beer on the wall.\n"
            elif i == 2:
                output_str += f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i - 1} bottle of beer on the wall.\n"
            elif i == 1:
                output_str += f"{i} bottle of beer on the wall, {i} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n"
            elif i == 0:
                output_str += "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
    else:
        output_str = None

    return output_str

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Esolang Interpreters #1  #####################################################################################################
                                                                                                  #  MiniStringFuck - 6 kyu   #


"""The Language
MiniStringFuck is a derivative of the famous Brainfuck which contains a memory cell as its only form of data storage as opposed to a memory tape of 30,000 cells in Brainfuck. The memory cell in MiniStringFuck initially starts at 0. MiniStringFuck contains only 2 commands as opposed to 8:

+ - Increment the memory cell. If it reaches 256, wrap to 0.
. - Output the value of the memory cell as a character with code point equal to the value
For example, here is a MiniStringFuck program that outputs the string "Hello, World!":
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."""

def MSF_interpreter(code: str) -> str:
    mem_cell: int = 0
    mem_array: list[int] = []
    output_str: str = ""

    for i in range(len(code)):
        if code[i] == "+": #Increment as needed
            mem_cell += 1
            if mem_cell == 256: #Ensure it is an 8 bit cell
                mem_cell = 0
        elif code[i] == ".":
            mem_array.append(mem_cell) #Output the cell into an int array
        
    for i in range(len(mem_array)): #Translate the int array to ASCII chars
        output_str += chr(mem_array[i])

    return output_str

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Esolang Interpreters #2  #####################################################################################################
                                                                                                  #   Smallfuck - 5 kyu   #


"""Here are a list of commands in Smallfuck:

> - Move pointer to the right (by 1 cell)
< - Move pointer to the left (by 1 cell)
* - Flip the bit at the current cell
[ - Jump past matching ] if value at current cell is 0
] - Jump back to matching [ (if value at current cell is nonzero)

The Task
Implement a custom Smallfuck interpreter interpreter() (interpreter in Haskell and F#, Interpreter in C#, custom_small_fuck:interpreter/2 in Erlang) which accepts the following arguments:

code - Required. The Smallfuck program to be executed, passed in as a string. May contain non-command characters. Your interpreter should simply ignore any non-command characters.
tape - Required. The initial state of the data storage (tape), passed in as a string. For example, if the string "00101100" is passed in then it should translate to something of this form within your interpreter: [0, 0, 1, 0, 1, 1, 0, 0]. You may assume that all input strings for tape will be non-empty and will only contain "0"s and "1"s.
Your interpreter should return the final state of the data storage (tape) as a string in the same format that it was passed in. For example, if the tape in your interpreter ends up being [1, 1, 1, 1, 1] then return the string "11111".
"""

def interpreter(code, tape):
    bit_array: list[int] = []
    code_pointer: int = 0
    tape_pointer: int = 0
    output_string: str = ""
    start_stack: list[int] = [] #LiFo
    end_stack: list[int] = [] #FiFo

    for i in range(len(tape)):
        bit_array.append(int(tape[i]))

    while code_pointer < len(code):
        if code[code_pointer] == ">":
            tape_pointer += 1
            if tape_pointer > len(bit_array) -1 :
                break
            
            
        elif code[code_pointer] == "<":
            tape_pointer -= 1
            if tape_pointer < 0:
                break
            
            
        elif code[code_pointer] == "*" and bit_array[tape_pointer] == 0:
            bit_array[tape_pointer] = 1

        elif code[code_pointer] == "*" and bit_array[tape_pointer] == 1:
            bit_array[tape_pointer] = 0

        elif code[code_pointer] == "[" and code_pointer not in start_stack:
            start_stack.append(code_pointer)
            sub_code_pointer: int = code_pointer
            
            while len(start_stack) != len(end_stack) and sub_code_pointer < len(code): #map the loop/nested loops
                sub_code_pointer += 1
                if code[sub_code_pointer] == "[":
                    start_stack.append(sub_code_pointer)
                elif code[sub_code_pointer] == "]":
                    end_stack.append(sub_code_pointer)
            

            if len(start_stack) > len(end_stack) and sub_code_pointer == len(code): #loop marker mismatch handling
                raise ValueError(f"Unclosed loop-start marker [ found at {start_stack[-1]}. Each open [ marker must have a closing ] marker pair.")
            elif len(start_stack) < len(end_stack) and sub_code_pointer == len(code):
                raise ValueError(f"Uninitiated loop-end marker ] found at {end_stack[0]}. Each open [ marker must have a closing ] marker pair.")

            code_pointer -= 1 #jump back to evaluate the first [ in the next iteration
   
        elif code[code_pointer] == "[" and code_pointer in start_stack: #eval the start of the mapped loop/loops
            if bit_array[tape_pointer] == 0: #if bit array position is 0 jump to loop close
                start_stack_index: int = start_stack.index(code_pointer) # Find the index of the current start marker
                code_pointer = end_stack[-(start_stack_index + 1)] #no -1 offset as we don't eval loop close in the next loop iter step
        
        elif code[code_pointer] == "]" and code_pointer not in end_stack: #loop marker mismatch handling
            raise ValueError(f"Uninitiated loop-end marker ] found at {code_pointer}. Each close [ marker must have an opening ] marker pair.")

        elif code[code_pointer] == "]" and code_pointer in end_stack: #eval the end of the mapped loop/loops
            if bit_array[tape_pointer] == 1:  # If current bit is 1, jump back to corresponding start
                end_stack_index: int = end_stack.index(code_pointer)  # Find the index of the current end marker
                code_pointer = start_stack[-(end_stack_index + 1)] - 1 # -1 offset as we don't eval loop close in the next loop iter step
            else:
                # If current bit is 0, exit the current loop
                start_stack.pop()
                end_stack.pop(0)

        code_pointer += 1 #next loop iter, move code pointer
        

    for i in range(len(bit_array)):
        output_string += str(bit_array[i])

    return output_string

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Esolang Interpreters #3  #####################################################################################################
                                                                                                  #   Paintfuck - 5 kyu   #


"""Valid commands in Paintfuck include:

n - Move data pointer north (up)
e - Move data pointer east (right)
s - Move data pointer south (down)
w - Move data pointer west (left)
* - Flip the bit at the current cell (same as in Smallfuck)
[ - Jump past matching ] if bit under current pointer is 0 (same as in Smallfuck)
] - Jump back to the matching [ (if bit under current pointer is nonzero) (same as in Smallfuck)

Your task is to implement a custom Paintfuck interpreter interpreter()/Interpret which accepts the following arguments in the specified order:

code - Required. The Paintfuck code to be executed, passed in as a string. May contain comments (non-command characters), in which case your interpreter should simply ignore them. If empty, simply return the initial state of the data grid.
iterations - Required. A non-negative integer specifying the number of iterations to be performed before the final state of the data grid is returned. See notes for definition of 1 iteration. If equal to zero, simply return the initial state of the data grid.
width - Required. The width of the data grid in terms of the number of data cells in each row, passed in as a positive integer.
height - Required. The height of the data grid in cells (i.e. number of rows) passed in as a positive integer."""

def PaintFck_interpreter(code: str, iterations: int, width: int, height: int) -> str:
    ##Argument type checks
    if not isinstance(code, (str)):
        raise ValueError(f"The code argument must be of type string.")
    elif not isinstance(iterations, (int)):
        raise ValueError(f"The iterations argument must be of type integer.")
    elif not isinstance(width, (int)):
        raise ValueError(f"The width argument must be of type integer.")
    elif not isinstance(height, (int)):
        raise ValueError(f"The height argument must be of type integer.")
    elif width < 0 or height < 0:
        raise ValueError(f"The width: {width} and height: {height} arguments must be positive integers.")
    
    ##Variable initializations
    bit_matrix: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
    code_pointer: int = 0
    row_pointer: int = 0
    col_pointer: int = 0
    output_string: str = ""
    loop_map: dict[int | int] = {} #a dict to hold loop start end coordinate pairs
    stack: list[int] = [] #LiFo

    ##Loop mapping - this is an improvement over the two stack solution
    def map_loops(code_to_map: str) -> dict[int | int]:
        for i in range(len(code_to_map)):
            if code_to_map[i] == "[":
                stack.append(i) #push the start index to the stack

            elif code_to_map[i] == "]" and len(stack) == 0: # error handling
                raise ValueError(f"Uninitiated loop-end marker ] found at {i}. Each open [ marker must have a closing ] marker pair.")
            
            elif code_to_map[i] == "]" and len(stack) != 0: #if close point found pop the corresponding opening from the stack and save the pair in the map
                loop_start: int = stack.pop() #pop the opening index
                loop_map[loop_start] = i #pair the closing index
                loop_map[i] = loop_start #map backwards too for backwards jumping

            elif len(stack) > 0 and i == len(code_to_map):
                raise ValueError(f"Unclosed loop-start marker [ found at {stack}. Each open [ marker must have a closing ] marker pair.")
            
        return loop_map
    
    loop_map = map_loops(code_to_map=code)
    
    ##Main interpreter loop
    while iterations > 0 and code_pointer < len(code):
        
        if code[code_pointer] == "n": #n - Move data pointer north (up)
            row_pointer -= 1
            if row_pointer < 0:
                row_pointer = len(bit_matrix) - 1
            
            iterations -= 1
        
        elif code[code_pointer] == "e": #e - Move data pointer east (right)
            col_pointer += 1
            if col_pointer > len(bit_matrix[0]) - 1: #assumes a matrix with equal length rows
                col_pointer = 0
            
            iterations -= 1
        
        elif code[code_pointer] == "s": #s - Move data pointer south (down)
            row_pointer += 1
            if row_pointer > len(bit_matrix) - 1:
                row_pointer = 0
            
            iterations -= 1

        elif code[code_pointer] == "w": #w - Move data pointer west (left)
            col_pointer -= 1
            
            if col_pointer < 0:
                col_pointer = len(bit_matrix[0]) - 1 #assumes a matrix with equal length rows
            
            iterations -= 1

        #elif code[code_pointer] in ["N", "E", "S", "W"]:
        #    raise ValueError(f"The movement instruction: {code[code_pointer]} at position {code_pointer} should be given in lower case.")
        
        elif code[code_pointer] == "*":
            bit_matrix[row_pointer][col_pointer] = 1 - bit_matrix[row_pointer][col_pointer]
            
            iterations -= 1

        elif code[code_pointer] == "[": #eval the start of the mapped loop/loops
            if bit_matrix[row_pointer][col_pointer] == 0: #if bit matrix position is 0 jump to loop close
                code_pointer = loop_map.get(code_pointer)

            iterations -= 1

        elif code[code_pointer] == "]": #eval the end of the mapped loop/loops
            if bit_matrix[row_pointer][col_pointer] == 1:  # If current bit is 1, jump back to corresponding start
                code_pointer = loop_map.get(code_pointer)

            iterations -= 1 

        code_pointer += 1
        
    for r in range(len(bit_matrix)):
            for c in range(len(bit_matrix[r])):
                if c == len(bit_matrix[r]) - 1 and r < len(bit_matrix) - 1:
                    output_string += str(bit_matrix[r][c]) + "\r\n"
                else:
                    output_string += str(bit_matrix[r][c])

    return output_string
        
###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Esolang Interpreters #4  #####################################################################################################
                                                                                                  #   Boolfuck - 3 kyu   #

"""Anyway, here is a list of commands and their descriptions:

+ - Flips the value of the bit under the pointer
, - Reads a bit from the input stream, storing it under the pointer. The end-user types information using characters, though. Bytes are read in little-endian order—the first bit read from the character a, for instance, is 1, followed by 0, 0, 0, 0, 1, 1, and finally 0. If the end-of-file has been reached, outputs a zero to the bit under the pointer.
; - Outputs the bit under the pointer to the output stream. The bits get output in little-endian order, the same order in which they would be input. If the total number of bits output is not a multiple of eight at the end of the program, the last character of output gets padded with zeros on the more significant end.
< - Moves the pointer left by 1 bit
> - Moves the pointer right by 1 bit
[ - If the value under the pointer is 0 then skip to the corresponding ]
] - Jumps back to the matching [ character, if the value under the pointer is 1"""

def BoolFck_interpreter(code: str, input: str = "") -> str:
    ##Argument type checks
    if not isinstance(code, (str)):
        raise ValueError(f"The code argument must be of type string.")
    elif not isinstance(input, (str)):
        raise ValueError(f"The input argument must be of type string.")

    ##Initialize variables
    code_pointer: int = 0
    memory_pointer: int = 0
    memory_bit_array: list[int] = [0]
    input_pointer: int = 0
    input_bit_array: list[int] = []
    output_string: str = ""
    output_bit_array: list[int] = []
    output_byte_array: list[int] = []
    loops: dict[int | int] = {}
    
    ##Loop mapping function
    def map_loops(code_to_map: str) -> dict:
        stack: list[int] = []
        loop_map: dict[int | int] = {}
        
        for i in range(len(code_to_map)):
            if code_to_map[i] == "[":
                stack.append(i)

            elif code_to_map[i] == "]" and len(stack) == 0:
                raise ValueError(f"Uninitiated loop-end marker ] found at {i}. Each open [ marker must have a closing ] marker pair.")
            
            elif code_to_map[i] == "]":
                loop_start: int = stack.pop()
                loop_map[loop_start] = i
                loop_map[i] = loop_start

            elif len(stack) > 0 and i == len(code_to_map):
                raise ValueError(f"Unclosed loop-start marker [ found at {stack}. Each open [ marker must have a closing ] marker pair.")
        
        return loop_map
    
    ##Input reading function
    def read_input_stream(input_stream: str) -> list[int]:
        input_byte: int = 0
        bit_lst: list[list[str]] = []
        bit_string: list[int] = []

        for i in range(len(input_stream)):
            input_byte = ord(input_stream[i])
            bit_lst.append(list(format(input_byte, "b")))

            while len(bit_lst[i]) < 8:
                bit_lst[i].insert(0, "0")
            
            bit_lst[i].reverse()
            bit_string.extend(int(bit) for bit in bit_lst[i])

        return bit_string

    loops = map_loops(code)
    input_bit_array = read_input_stream(input)
            
    ##Main interpreter loop
    while code_pointer < len(code):
        
        if code[code_pointer] == "<":
            memory_pointer -= 1
            if memory_pointer < 0:
                memory_bit_array.insert(0, 0)
                memory_pointer = 0

        elif code[code_pointer] == ">":
            memory_pointer += 1
            if memory_pointer >= len(memory_bit_array):
                memory_bit_array.append(0)

        elif code[code_pointer] == "+":
            memory_bit_array[memory_pointer] = 1 - memory_bit_array[memory_pointer]
        
        elif code[code_pointer] == "," and len(input_bit_array) > 0:
            if input_pointer >= len(input_bit_array):
                memory_bit_array[memory_pointer] = 0
            else:
                memory_bit_array[memory_pointer] = input_bit_array[input_pointer]
            input_pointer += 1
                

        elif code[code_pointer] == ";":
            output_bit_array.append(memory_bit_array[memory_pointer])

        elif code[code_pointer] == "[": #eval the start of the mapped loop/loops
            if memory_bit_array[memory_pointer] == 0: #if bit matrix position is 0 jump to loop close
                code_pointer = loops.get(code_pointer)

        elif code[code_pointer] == "]": #eval the end of the mapped loop/loops
            if memory_bit_array[memory_pointer] == 1:  # If current bit is 1, jump back to corresponding start
                code_pointer = loops.get(code_pointer) 

        code_pointer += 1

    ##Convert output string
    def byte_array_converter(bit_array: list[int]) -> list[int]:
        byte_lst: list[int] = []
        byte: list[int] = []
        

        for i in range(len(bit_array)):
            byte.append(bit_array[i])
            
            if len(byte) == 8:
                byte.reverse()
                number: int = 0

                for e in range(len(byte)):
                    number = (number << 1) | byte[e]
                
                byte_lst.append(number)
                byte.clear()
            
        if len(byte) > 0:
                
            while len(byte) < 8:
                byte.append(0)
                
            byte.reverse()
            number: int = 0

            for e in range(len(byte)):
                number = (number << 1) | byte[e]
                
            byte_lst.append(number)
            byte.clear()

        return byte_lst
    
    output_byte_array = byte_array_converter(output_bit_array)
    

    ##Convert output byte array to string
    for i in range(len(output_byte_array)): #Translate the int array to ASCII chars
        output_string += chr(output_byte_array[i])

    return output_string

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Esolang Interpreters #5  #####################################################################################################
                                                                                                  #   Befunge - 4 kyu   #

"""
Your task is to write a method which will interpret Befunge-93 code! Befunge-93 is a language in which the code is presented not as a series of instructions, but as instructions scattered on a 2D plane; your pointer starts at the top-left corner and defaults to moving right through the code. Note that the instruction pointer wraps around the screen! There is a singular stack which we will assume is unbounded and only contain integers. While Befunge-93 code is supposed to be restricted to 80x25, you need not be concerned with code size. Befunge-93 supports the following instructions (from Wikipedia):

0-9 Push this number onto the stack.
+ Addition: Pop a and b, then push a+b.
- Subtraction: Pop a and b, then push b-a.
* Multiplication: Pop a and b, then push a*b.
/ Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
% Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
` (backtick) Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
> Start moving right.
< Start moving left.
^ Start moving up.
v Start moving down.
? Start moving in a random cardinal direction.
_ Pop a value; move right if value = 0, left otherwise.
| Pop a value; move down if value = 0, up otherwise.
" Start string mode: push each character's ASCII value all the way up to the next ".
: Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
\ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.
$ Pop value from the stack and discard it.
. Pop value and output as an integer.
, Pop value and output the ASCII character represented by the integer code that is stored in the value.
# Trampoline: Skip next cell.
p A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at the position (x,y) in the program to the character with ASCII value v.
g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character at that position in the program.
@ End program.
  (i.e. a space) No-op. Does nothing.
The above list is slightly modified: you'll notice if you look at the Wikipedia page that we do not use the user input instructions and dividing by zero simply yields zero.
"""


import time

def interpret(code):
    ##Initialize variables
    code_matrix: list[list[str]] = [[" " for _ in range(80)] for _ in range(25)]
    stack: list[int] = []
    code_pointer: dict[str | int] = {"row" : 0, "col" : 0}
    move_dir: str = "e"
    output: str = ""

    def construct_code_matrix(code_to_mat: str, matrix: list[list[str]]) -> list[list[str]]:
        x: int = 0
        y: int = 0
        c_matrix = [row.copy() for row in matrix]  # Deep copy each row, otherwise the nested lists are not copied, only referenced...

        for i in range(len(code_to_mat)):
            if code_to_mat[i] == "\n":
                y += 1
                x = 0
                continue
            
            c_matrix[y][x] = code_to_mat[i]
            x += 1

        return c_matrix
    
    def move() -> None:
        if move_dir == "e":
            code_pointer["col"] += 1
            if code_pointer["col"] == len(code_matrix[0]):
                    code_pointer["col"] = 0
        elif move_dir == "w":
            code_pointer["col"] -= 1
            if code_pointer["col"] < 0:
                    code_pointer["col"] = len(code_matrix[0]) - 1 #fixed toroidal wrapping
        elif move_dir == "s":
            code_pointer["row"] += 1
            if code_pointer["row"] == len(code_matrix):
                    code_pointer["row"] = 0
        elif move_dir == "n":
            code_pointer["row"] -= 1
            if code_pointer["row"] < 0:
                    code_pointer["row"] = len(code_matrix) - 1 #fixed toroidal wrapping

    def random_int_generator() -> str: #8-bit xorshift RNG
        random_int: int = int()
        random_value_range: int = 5
        max_8bit_range: int = 256
        output_int: int = int()

        #Apply rejection sampling correction (needed if the raw range size is not a multiple of the draw range size)
        corrected_range: int = max_8bit_range - (max_8bit_range % random_value_range)

        while True:
            seed: int = int(time.time() * 10000)
            random_int = (seed ^ (seed << 3)) & 0xFF
            random_int = (random_int ^ (random_int >> 2)) & 0xFF
            random_int = (random_int ^ (random_int << 1)) & 0xFF
            
            if random_int < corrected_range:
                output_int = random_int % random_value_range
                break

        return output_int

    
    code_matrix = construct_code_matrix(code_to_mat = code, matrix = code_matrix)

    break_counter: int = 0
    end_process: bool = False
    while end_process == False and break_counter < 10000:
        
        
        if code_matrix[code_pointer["row"]][code_pointer["col"]] == ">":
            move_dir = "e"

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "v":
            move_dir = "s"

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "<":
            move_dir = "w"

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "^":
            move_dir = "n"

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "?":
            new_direction: int = random_int_generator()
            if new_direction == 0:
                move_dir = "n"
            elif new_direction == 1:
                move_dir = "e"
            elif new_direction == 2:
                move_dir = "s"
            elif new_direction == 3:
                move_dir = "w"
        
        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "_":
            new_direction: int = stack.pop()
            if new_direction == 0:
                move_dir = "e"
            else:
                move_dir = "w"
        
        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "|":
            new_direction: int = stack.pop()
            if new_direction == 0:
                move_dir = "s"
            else:
                move_dir = "n"

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            stack.append(int(code_matrix[code_pointer["row"]][code_pointer["col"]]))

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "+":
            if len(stack) > 1:
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(a + b)
            
            elif len(stack) == 1:
                a: int = stack.pop()
                b: int = 0
                stack.append(a + b)

            elif len(stack) == 0:
                a: int = 0
                b: int = 0
                stack.append(a + b)


        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "-":
            if len(stack) > 1:
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(b - a)
            
            elif len(stack) == 1:
                a: int = stack.pop()
                b: int = 0
                stack.append(b - a)

            elif len(stack) == 0:
                a: int = 0
                b: int = 0
                stack.append(b - a)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "*":
            if len(stack) > 1:
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(a * b)
            
            elif len(stack) == 1:
                stack.pop()
                stack.append(0)

            elif len(stack) == 0:
                stack.append(0)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "/":
            if len(stack) > 1:
                a: int = stack.pop()
                b: int = stack.pop()
                if a == 0:
                    stack.append(0)
                else:
                    stack.append(b // a)

            elif len(stack) == 1:
                stack.pop()
                stack.append(0)

            elif len(stack) == 0:
                stack.append(0)
                

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "%":
            a: int = stack.pop()
            b: int = stack.pop()
            if a == 0:
                stack.append(0)
            else:
                stack.append(b % a)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "!":
            a: int = stack.pop()
            if a == 0:
                stack.append(1)
            else:
                stack.append(0)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "`":
            a: int = stack.pop()
            b: int = stack.pop()
            if b > a:
                stack.append(1)
            else:
                stack.append(0)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == '"':
            move()
            while code_matrix[code_pointer["row"]][code_pointer["col"]] != '"':
                stack.append(ord(code_matrix[code_pointer["row"]][code_pointer["col"]]))
                move()
        
        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == ":":
            if len(stack) >= 1:
                duplicate_val: int = stack[-1]
                stack.append(duplicate_val)
            
            elif len(stack) == 0:
                stack.append(0)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "\\":
            if len(stack) > 1:
                a: int = stack.pop()
                b: int = stack.pop()

                stack.append(a)
                stack.append(b)
            
            elif len(stack) == 1:
                a: int = stack.pop()

                stack.append(a)
                stack.append(0)

            elif len(stack) == 0:
                for i in range(2):
                    stack.append(0)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "$":
            if len(stack) >= 1:
                stack.pop()

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == ".":
                if len(stack) >= 1:
                    output += str(stack.pop())
                else:
                    output += str(0)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == ",":
                if len(stack) >= 1:
                    output += chr(stack.pop())
                else:
                    output += chr(0)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "#":
            move()

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "p":
            y: int = stack.pop()
            x: int = stack.pop()
            v: int = stack.pop()

            code_matrix[y][x] = chr(v)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "g":
            y: int = stack.pop()
            x: int = stack.pop()
            
            stack.append(ord(code_matrix[y][x]))

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "&":
            while True:
                try:
                    input_val: str = input("Please provide an integer to be pushed onto the stack \n: ")
                    input_int: int = int(input_val)
                    break

                except ValueError:
                    print(f"the input you entered {input_val} cannot be turned into an integer. Please try again!")

            stack.append(input_int)

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "~":
            input_char: str = ""
            input_char = input("Please provide a character, for it's ASCII value to be pushed onto the stack \n: ")
            
            while len(input_char) != 1:
                input_char = input("The length of the input you provided is larger than 1. Please enter a single character \n: ")

            stack.append(ord(input_char))

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "" or code_matrix[code_pointer["row"]][code_pointer["col"]] == " ":
            pass

        elif code_matrix[code_pointer["row"]][code_pointer["col"]] == "@":
            end_process = True

        
        move()
        break_counter += 1 
        
    return output

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Esolang Interpreters #6  #####################################################################################################
                                                                                                  #   Simple assembler - 5 kyu   #

"""
We want to create a simple interpreter of assembler which will support the following instructions:

mov x y - copies y (either a constant value or the content of a register) into register x
inc x - increases the content of the register x by one
dec x - decreases the content of the register x by one
jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), but only if x (a constant or a register) is not zero
Register names are alphabetical (letters only). Constants are always integers (positive or negative).

Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the program instructions and will execute them. The program ends when there are no more instructions to execute, then it returns a dictionary (a table in COBOL) with the contents of the registers.

Also, every inc/dec/jnz on a register will always be preceeded by a mov on the register first, so you don't need to worry about uninitialized registers.
"""

def simple_assembler(program):
    code_list: list[str] = program.copy()
    instruction_pointer: int = 0
    instructions: list[list[str]] = []
    current_instruction: dict[str | str] = {}
    registers: dict[str | int] = {}
    registers_to_pop: list[str] = []

    def tokenizer(code_lst: list[str]) -> None:
        for i in range(len(code_lst)):
            instruction: str = code_lst[i]
            instructions.append(instruction.split(sep=" "))

        return None
    
    def load_instruction(inst_lst: list[list[str]], ip: int) -> None:
        instr: list[str] = inst_lst[ip]

        if len(instr) == 2:
            current_instruction.update({"instruction" : instr[0], "arg1" : instr[1], "arg2" : None})
        elif len(instr) == 3:
            if instr[2].lstrip("-").isdigit():
                current_instruction.update({"instruction" : instr[0], "arg1" : instr[1], "arg2" : int(instr[2])})
            else:
                current_instruction.update({"instruction" : instr[0], "arg1" : instr[1], "arg2" : instr[2]})
        else:
            raise IndexError("There are no instructions in the instruction list")

        return None
    
    def map_registers(inst_lst: list[str]) -> None:
        char_list: list[str] = [chr(_) for _ in range(ord("a"), ord("z") + 1)]
        
        for i in range(len(inst_lst)):
            load_instruction(inst_lst = inst_lst, ip = i)

            if current_instruction["arg1"] in char_list and current_instruction["arg1"] not in registers.keys():
                registers.update({current_instruction["arg1"] : None})
            elif current_instruction["arg2"] in char_list and current_instruction["arg2"] not in registers.keys():
                registers.update({current_instruction["arg2"] : None})
            else:
                pass
        
        return None
    
    def jump_test(x):
        if x.isdigit():
            return x
        else:
            return registers[x]

    tokenizer(code_list)
    map_registers(instructions)
    
    while instruction_pointer >= 0 and instruction_pointer < len(code_list):
        load_instruction(inst_lst = instructions, ip = instruction_pointer)

        if current_instruction["instruction"] == "mov":
            if isinstance(current_instruction["arg2"], int):
                registers[current_instruction["arg1"]] = current_instruction["arg2"]
            elif isinstance(current_instruction["arg2"], str):
                registers[current_instruction["arg1"]] = registers[current_instruction["arg2"]]
        
        elif current_instruction["instruction"] == "inc":
            registers[current_instruction["arg1"]] += 1

        elif current_instruction["instruction"] == "dec":
            registers[current_instruction["arg1"]] -= 1

        elif current_instruction["instruction"] == "jnz":
            if jump_test(current_instruction["arg1"]) != 0 and isinstance(current_instruction["arg2"], int):
                instruction_pointer = instruction_pointer + current_instruction["arg2"]
                continue

            elif jump_test(current_instruction["arg1"]) != 0 and isinstance(current_instruction["arg2"], str):
                instruction_pointer = instruction_pointer + registers[current_instruction["arg2"]]
                continue

            elif jump_test(current_instruction["arg1"]) == 0:
                pass

        instruction_pointer += 1

    for key in registers.keys():
        if registers[key] == None:
            registers_to_pop.append(key)
    
    for i in range(len(registers_to_pop)):
        registers.pop(registers_to_pop[i])
    
    return registers

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################  Esolang Interpreters #7  #####################################################################################################
                                                                                                  #   Assembler - 2 kyu   #

"""
We want to create an interpreter of assembler which will support the following instructions:

mov x, y - copy y (either an integer or the value of a register) into register x.
inc x - increase the content of register x by one.
dec x - decrease the content of register x by one.
add x, y - add the content of the register x with y (either an integer or the value of a register) and stores the result in x (i.e. register[x] += y).
sub x, y - subtract y (either an integer or the value of a register) from the register x and stores the result in x (i.e. register[x] -= y).
mul x, y - same with multiply (i.e. register[x] *= y).
div x, y - same with integer division (i.e. register[x] /= y).
label: - define a label position (label = identifier + ":", an identifier being a string that does not match any other command). Jump commands and call are aimed to these labels positions in the program.
jmp lbl - jumps to the label lbl.
cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value of a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
je lbl - jump to the label lbl if the values of the previous cmp command were equal.
jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
jl lbl - jump to the label lbl if x was less than y in the previous cmp command.
call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction pointer should return to the instruction next to this call command.
ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that called the current function.
msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.
end - this instruction indicates that the program ends correctly, so the stored output is returned (if the program terminates without this instruction it should return the default output: see below).
; comment - comments should not be taken in consideration during the execution of the program.

Output format:
The normal output format is a string (returned with the end command). For Scala and Rust programming languages it should be incapsulated into Option.

If the program does finish itself without using an end instruction, the default return value is:

-1 (as an integer)
"""

#----- Define classes -----#
class Token:
    def __init__(self, type: str = None, value: str = None) -> None:
        self.type: str = type
        self.value: str = value

    def __str__(self) -> str:
        return f"Token(type = {self.type}, value = {self.value})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Instruction:

    def __init__(self, opcode: str, args: list[str | int | float]):
        self.opcode = opcode
        self.args = args

    def __str__(self) -> None:
        return f"Instruction(opcode = {self.opcode}, args = {self.args})"
    
    def __repr__(self) -> None:
        return self.__str__()

#----- Define sub-functions -----#
def lexer(instructions: list[str], instruction_set: list[str]) -> list[Token]:
    token_lst: list[Token] = []


    def operand_classifier(operand: str) -> Token:
        if operand.isdigit():
            return Token(type = "INT", value = operand)
                                
        elif operand.find(".") != -1:
            return Token(type = "FLOAT", value = operand)
                                
        else:
            return Token(type = "IDENT", value = operand)
    

    for i in range(len(instructions)):
        if not instructions[i]:
                continue
        
        instruction: str = instructions[i].strip()

        if  instruction.startswith(";"):
            continue

        elif instruction.find(";") != -1:
            instruction = instruction.split(";", 1)[0]
            
        if  instruction.endswith(":"):
            label_end: int =  instruction.find(":")
                
            token_lst.append(Token(type = "LABEL", value =  instruction[0 : label_end]))
        
        elif instruction == "end" or  instruction == "ret":
            token_lst.append(Token(type = "OPCODE", value =  instruction))

        else:
            opcode: str = instruction.split(" ", 1)[0]

            if opcode in instruction_set and opcode not in [";", ":", "end", "ret"]:
                operands: str = instruction.split(" ", 1)[1].strip()

                if opcode == "msg" and "," in operands:
                    token_lst.append(Token(type = "OPCODE", value = "msg"))
                    operand_lst: list[str] = []
                    char_pointer: int = 0
                    
                    while char_pointer < len(operands):
                        
                        if operands[char_pointer] == "'" or operands[char_pointer] == '"':
                            string_end: str = operands[char_pointer]
                            sub_char_p: int = char_pointer + 1
                            message: str = ""
                            
                            while sub_char_p < len(operands) and operands[sub_char_p] != string_end:
                                message += operands[sub_char_p]
                                
                                sub_char_p += 1

                            operand_lst.append("'" + message + "'")
                            char_pointer = sub_char_p
                        
                        else:
                            string_marker: set = {"'", '"'}
                            sub_char_p: int = char_pointer
                            sub_string: str = ""

                            while sub_char_p < len(operands) and operands[sub_char_p] not in string_marker:
                                sub_string += operands[sub_char_p]

                                sub_char_p += 1

                            operand_lst.append(sub_string)
                            char_pointer = sub_char_p -1

                        char_pointer += 1
                    
                    for operand in operand_lst:
                        if operand.startswith("'"):
                            token_lst.append(Token(type = "MESSAGE", value = operand))
                        
                        else:
                            token_lst.append(operand_classifier(operand = operand.replace(",", "").strip()))
                        
                elif opcode == "msg" and "," not in operands:
                    token_lst.append(Token(type = "OPCODE", value = "msg"))
                    
                    if operands.startswith("'") or operands.startswith('"'):
                        message_start: str = operands[0]
                    
                        token_lst.append(Token(type = "MESSAGE", value = "'" + operands.strip(message_start).strip() + "'"))

                    else:
                        token_lst.append(operand_classifier(operand = operands.strip()))

                else:
                    token_lst.append(Token(type = "OPCODE", value = opcode))
                    operands = operands.replace(" ", "")

                    if "," in operands:
                        operand_lst = operands.split(",")
                        
                        for e in range(len(operand_lst)):
                            token_lst.append(operand_classifier(operand = operand_lst[e]))

                    else:
                        token_lst.append(operand_classifier(operand = operands))

            elif opcode not in instruction_set:
                raise ValueError(f"The given opcode {opcode} is not part of the valid instruction set.")

    return token_lst

def parser(token_list: list[Token]) -> tuple[list[Instruction], dict[str, int]]:
    token_lst: list[Token] = token_list.copy()
    instruction_list: list[Instruction] = []
    jump_table: dict[str, int] = {}
    
    list_pointer: int = 0
    while list_pointer < len(token_lst):
        current_opcode: str = ""
        
        if token_lst[list_pointer].type in ("OPCODE", "LABEL"):
            if token_lst[list_pointer].type == "OPCODE":
                current_opcode = token_lst[list_pointer].value
            
            elif token_lst[list_pointer].type == "LABEL":
                jump_table[token_lst[list_pointer].value] = len(instruction_list)
                list_pointer += 1
                continue
            
            list_pointer += 1
            
            current_args: list[str | int | float] = []
            
            while list_pointer < len(token_lst) and token_lst[list_pointer].type not in ("OPCODE", "LABEL"):
        
                if token_lst[list_pointer].type == "INT":
                    current_args.append(int(token_lst[list_pointer].value))
                    list_pointer += 1
                        
                    
                elif token_lst[list_pointer].type == "FLOAT":
                    current_args.append(float(token_lst[list_pointer].value))
                    list_pointer += 1
                        

                elif token_lst[list_pointer].type == "IDENT":
                    current_args.append(token_lst[list_pointer].value)
                    list_pointer += 1
                
                elif token_lst[list_pointer].type == "MESSAGE":
                    current_args.append("'" + token_lst[list_pointer].value + "'")
                    list_pointer += 1
                
                else:
                    break
            
            instruction_list.append(Instruction(opcode = current_opcode, args = current_args))

    return instruction_list, jump_table

def register_mapper(instruction_list: Instruction, reg_opcodes: set[str]) -> dict[str, int]:
    instr_lst: list[Instruction] = instruction_list.copy()
    register_table: dict[str, int] = {}

    for i in range(len(instr_lst)):
        if instr_lst[i].opcode in reg_opcodes:
            
            for arg in instr_lst[i].args:
                if isinstance(arg, (str)):
                    register_table[arg] = 0

    return register_table

def syntax_analyzer(instruction_lst: list[Instruction], jump_tbl: dict[str, int], register_tbl: dict[str, int]) -> list[str]:
    error_list: list[str] = []

    for i, instruction in enumerate(instruction_lst):
        if instruction.opcode in ("mov", "add", "sub", "mul", "div"):
            if len(instruction.args) < 2:
                error_list.append(f"Instruction {i}: {instruction.opcode} expects exactly 2 arguments, less was given.")
            
            elif len(instruction.args) > 2:
                error_list.append(f"Instruction {i}: {instruction.opcode} expects exactly 2 arguments, more was given.")

            if not isinstance(instruction.args[0], (str)):
                error_list.append(f"Instruction {i}: {instruction.opcode} expects a register name as a first argument, none str type was given.")

            elif isinstance(instruction.args[0], (str)) and instruction.args[0] not in register_tbl.keys():
                error_list.append(f"Instruction {i}: {instruction.opcode} expects a valid register name as a first argument, the given name is not part of the mapped registers.")
            
            if isinstance(instruction.args[1], (str)) and instruction.args[1] not in register_tbl.keys():
                error_list.append(f"Instruction {i}: {instruction.opcode} expects an int, float or a valid register name as the second argument, the given name is not part of the mapped registers.")

        elif instruction.opcode in ("inc", "dec"):
            if len(instruction.args) < 1:
                error_list.append(f"Instruction {i}: {instruction.opcode} expects exactly 1 argument, less was given.")
            
            elif len(instruction.args) > 1:
                error_list.append(f"Instruction {i}: {instruction.opcode} expects exactly 1 argument, more was given.")

            if not isinstance(instruction.args[0], (str)):
                error_list.append(f"Instruction {i}: {instruction.opcode} expects a register name as an argument, none str type was given.")

            elif isinstance(instruction.args[0], (str)) and instruction.args[0] not in register_tbl.keys():
                error_list.append(f"Instruction {i}: {instruction.opcode} expects a valid register name as an argument, the given name is not part of the mapped registers.")

        elif instruction.opcode in ("jmp", "jne", "je", "jge", "jg", "jle", "jl", "call"):
            if len(instruction.args) < 1:
                error_list.append(f"Instruction {i}: {instruction.opcode} expects exactly 1 argument, less was given.")
            
            elif len(instruction.args) > 1:
                error_list.append(f"Instruction {i}: {instruction.opcode} expects exactly 1 argument, more was given.")

            if not isinstance(instruction.args[0], (str)):
                error_list.append(f"Instruction {i}: {instruction.opcode} expects a label of type str as an argument, none str type was given.")

            elif isinstance(instruction.args[0], (str)) and instruction.args[0] not in jump_tbl.keys():
                error_list.append(f"Instruction {i}: {instruction.opcode} expects a valid label argument, the given label is not part of the mapped labels.")
            
        elif instruction.opcode == "cmp":
            if len(instruction.args) < 2:
                error_list.append(f"Instruction {i}: 'cmp' expects exactly 2 arguments, less was given.")
            
            elif len(instruction.args) > 2:
                error_list.append(f"Instruction {i}: 'cmp' expects exactly 2 arguments, more was given.")

            elif isinstance(instruction.args[0], (str)) and instruction.args[0] not in register_tbl.keys():
                error_list.append(f"Instruction {i}: 'cmp' expects an int, float or a valid register name as a first argument, the given name is not part of the mapped registers.")
            
            if isinstance(instruction.args[1], (str)) and instruction.args[1] not in register_tbl.keys():
                error_list.append(f"Instruction {i}: 'cmp' expects an int, float or a valid register name as the second argument, the given name is not part of the mapped registers.")

        elif instruction.opcode == "msg":
            for e, arg in enumerate(instruction.args):
                if not isinstance(arg, (str)):
                    error_list.append(f"Instruction {i}: {instruction.opcode} expects a character strings or valid register names arguments, argument {e} is not of type str.")

                elif isinstance(arg, (str)) :
                    if not (arg.startswith("'") and arg.endswith("'")) and arg not in register_tbl.keys():
                        error_list.append(f"Instruction {i}: {instruction.opcode} argument {e} is neither a valid register nor a string literal.")

        elif instruction.opcode in ("ret", "end"):
            if len(instruction.args) != 0:
                error_list.append(f"Instruction {i}: {instruction.opcode} expects no argument, but some was given.")

    return error_list

def code_executor(instruction_lst: list[Instruction], jump_tbl: dict[str, int], register_tbl: dict[str, int]) -> str | int:
    output_str: str = ""
    call_stack: list[int] = []
    comp_results: dict[str, bool] = {
        "jne" : False,
        "je" : False,
        "jge" : False,
        "jg" : False,
        "jle" : False, 
        "jl" : False
    }
    ip: int = 0 #instruction pointer

    def reset_comp() -> None:
        for key in comp_results:
            comp_results[key] = False

    while ip < len(instruction_lst) and ip >= 0:
        if instruction_lst[ip].opcode == "mov":
            
            if isinstance(instruction_lst[ip].args[1], (int, float)):
                register_tbl[instruction_lst[ip].args[0]] = instruction_lst[ip].args[1]
            
            else:
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[1])

        elif instruction_lst[ip].opcode == "inc":
            register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) + 1

        elif instruction_lst[ip].opcode == "dec":
            register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) - 1

        elif instruction_lst[ip].opcode == "add":
            
            if isinstance(instruction_lst[ip].args[1], (int, float)):
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) + instruction_lst[ip].args[1]
            
            else:
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) + register_tbl.get(instruction_lst[ip].args[1])

        elif instruction_lst[ip].opcode == "sub":
            
            if isinstance(instruction_lst[ip].args[1], (int, float)):
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) - instruction_lst[ip].args[1]
            
            else:
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) - register_tbl.get(instruction_lst[ip].args[1])

        elif instruction_lst[ip].opcode == "mul":
            
            if isinstance(instruction_lst[ip].args[1], (int, float)):
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) * instruction_lst[ip].args[1]
            
            else:
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) * register_tbl.get(instruction_lst[ip].args[1])

        elif instruction_lst[ip].opcode == "div":
            
            if isinstance(instruction_lst[ip].args[1], (int, float)) and instruction_lst[ip].args[1] != 0:
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) // instruction_lst[ip].args[1]
            
            elif isinstance(instruction_lst[ip].args[1], (str)) and register_tbl.get(instruction_lst[ip].args[1]) != 0:
                register_tbl[instruction_lst[ip].args[0]] = register_tbl.get(instruction_lst[ip].args[0]) // register_tbl.get(instruction_lst[ip].args[1])
            
            else:
                print("Division by 0 is not comprehensible.")
                return -1

        elif instruction_lst[ip].opcode == "cmp":
            reset_comp()
            arg1: int | float = 0
            arg2: int | float = 0
            
            if isinstance(instruction_lst[ip].args[0], (int, float)) and isinstance(instruction_lst[ip].args[1], (int, float)):
                arg1 = instruction_lst[ip].args[0]
                arg2 = instruction_lst[ip].args[1]

            elif isinstance(instruction_lst[ip].args[0], (str)) and isinstance(instruction_lst[ip].args[1], (int, float)):
                arg1 = register_tbl.get(instruction_lst[ip].args[0])
                arg2 = instruction_lst[ip].args[1]

            elif isinstance(instruction_lst[ip].args[0], (int, float)) and isinstance(instruction_lst[ip].args[1], (str)):
                arg1 = instruction_lst[ip].args[0]
                arg2 = register_tbl.get(instruction_lst[ip].args[1])
            
            elif isinstance(instruction_lst[ip].args[0], (str)) and isinstance(instruction_lst[ip].args[1], (str)):
                arg1 = register_tbl.get(instruction_lst[ip].args[0])
                arg2 = register_tbl.get(instruction_lst[ip].args[1])

            if arg1 != arg2:
                comp_results["jne"] = True

            if arg1 > arg2:
                    comp_results["jg"] = True
            
            if arg1 < arg2:
                    comp_results["jl"] = True

            if arg1 == arg2:
                comp_results["je"] = True

            if arg1 >= arg2:
                comp_results["jge"] = True
            
            if arg1 <= arg2:
                comp_results["jle"] = True 
               
            
        elif instruction_lst[ip].opcode == "jmp":
            ip = jump_tbl.get(instruction_lst[ip].args[0])
            continue

        elif instruction_lst[ip].opcode in {"jne", "je", "jge", "jg", "jle", "jl"}:
            if comp_results.get(instruction_lst[ip].opcode) == True:
                ip = jump_tbl.get(instruction_lst[ip].args[0])
                
                continue
            else:
                ip += 1
                continue

        elif instruction_lst[ip].opcode == "call":
            call_stack.append(ip)
            ip = jump_tbl.get(instruction_lst[ip].args[0])
            continue

        elif instruction_lst[ip].opcode == "ret":
            if len(call_stack) > 0:
                ip = call_stack.pop() + 1
                continue

            else:
                return -1
            
        elif instruction_lst[ip].opcode == "msg":
            for arg in instruction_lst[ip].args:
                if isinstance(arg, (str)) and arg.startswith("'"):
                    output_arg: str = arg.strip("'")
                    output_str += output_arg
                    
                elif isinstance(arg, (str)):
                    if isinstance(register_tbl.get(arg), (float)) and register_tbl.get(arg).is_integer():
                        output_str += str(int(register_tbl.get(arg)))
                    else:
                        output_str += str(register_tbl.get(arg))
                    
        elif instruction_lst[ip].opcode == "end":
            return output_str.strip()
        
        else:
            break
        
        ip += 1

    return -1
        


    
#----- Define the main interpreter class -----#
class Interpreter:
    INSTRUCTION_SET: list[str] = ["mov", "inc", "dec", "add", "sub", "mul", "div", ":", "jmp",
                                 "cmp", "jne", "je", "jge", "jg", "jle", "jl", "call", "ret", 
                                 "msg", ";", "end"]
    REG_OPS: list[str] = ["mov", "inc", "dec", "add", "sub", "mul", "div"]
    
    def __init__(self, code) -> None:
        self.code: str = code
        self.line_pointer: int = 0
        self.instruction_set: list[str] = self.INSTRUCTION_SET
        self.register_opcodes: set[str] = self.REG_OPS
        self.preprocessed_code = self.code.split("\n")
        self.token_list: list[Token] = []
        self.instruction_list: list[Instruction] = []
        self.jump_table: dict[str, int] = {}
        self.register_table: dict[str, int | float] = {}
        self.error_list: list[str] = []
        self.output_stream: str | int = ""
        
        
    def __str__(self) -> str:
        return f"Program:\n< {len(self.preprocessed_code)} lines,\n{len(self.token_list)} tokens,\n{len(self.instruction_list)} instructions,\n{len(self.register_table)} registers >"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    
    def lex(self) -> None:
        self.token_list = lexer(instructions = self.preprocessed_code, instruction_set = self.instruction_set)

    def parse(self) -> None:
        self.instruction_list, self.jump_table = parser(token_list = self.token_list)

    def map_registers(self) -> None:
        self.register_table = register_mapper(instruction_list = self.instruction_list, reg_opcodes = self.register_opcodes)

    def analyze_syntax(self) -> None:
        self.error_list = syntax_analyzer(instruction_lst = self.instruction_list, jump_tbl = self.jump_table, register_tbl = self.register_table)

    def execute_code(self) -> None:
        self.output_stream = code_executor(instruction_lst = self.instruction_list, jump_tbl = self.jump_table, register_tbl = self.register_table)

    def interpret(self) -> None:
        self.lex()
        self.parse()
        self.map_registers()
        self.analyze_syntax()
        if len(self.error_list) != 0:
            raise SyntaxError(f"Syntax errors found in provided code:\n {self.error_list} ")
        self.execute_code()
        return self.output_stream

def assembler_interpreter(program):
    return Interpreter(program).interpret()

###################################################################################################  Kata end  #####################################################################################################






###################################################################################################     Esolang Interpreters #8     #####################################################################################################
                                                                                                  #   RoboScript series 1 - 6 kyu   #

"""
Your MyRobot-specific (esoteric) scripting language called RoboScript only ever contains the following characters: F, L, R, the digits 0-9 and brackets (( and )). Your goal is to write a function highlight which accepts 1 required argument code which is the RoboScript program passed in as a string and returns the script with syntax highlighting. The following commands/characters should have the following colors:

F - Wrap this command around <span style="color: pink"> and </span> tags so that it is highlighted pink in our editor
L - Wrap this command around <span style="color: red"> and </span> tags so that it is highlighted red in our editor
R - Wrap this command around <span style="color: green"> and </span> tags so that it is highlighted green in our editor
Digits from 0 through 9 - Wrap these around <span style="color: orange"> and </span> tags so that they are highlighted orange in our editor
Round Brackets - Do not apply any syntax highlighting to these characters
For example:

highlight("F3RF5LF7"); // => "<span style=\"color: pink\">F</span><span style=\"color: orange\">3</span><span style=\"color: green\">R</span><span style=\"color: pink\">F</span><span style=\"color: orange\">5</span><span style=\"color: red\">L</span><span style=\"color: pink\">F</span><span style=\"color: orange\">7</span>"
And for multiple characters with the same color, simply wrap them with a single <span> tag of the correct color:

highlight("FFFR345F2LL"); // => "<span style=\"color: pink\">FFF</span><span style=\"color: green\">R</span><span style=\"color: orange\">345</span><span style=\"color: pink\">F</span><span style=\"color: orange\">2</span><span style=\"color: red\">LL</span>"
Note that the use of <span> tags must be exactly the same format as demonstrated above. Even if your solution produces the same visual result as the expected answers, if you miss a space betwen "color:" and "green", for example, you will fail the tests.
"""

def highlight(code: str) -> str:
    return_string: str = ""

    char_index: int = 0
    while char_index < len(code):
        if code[char_index] == "F":
            return_string += '<span style="color: pink">'
            
            sub_index: int = char_index
            while sub_index < len(code) and code[sub_index] == "F":
                return_string += f"{code[sub_index]}"
                sub_index += 1
                char_index = sub_index - 1
            
            return_string += "</span>"

        elif code[char_index] == "L":
            return_string += '<span style="color: red">'

            sub_index: int = char_index
            while sub_index < len(code) and code[sub_index] == "L":
                return_string += f"{code[sub_index]}"
                sub_index += 1
                char_index = sub_index - 1

            return_string += "</span>"

        elif code[char_index] == "R":
            return_string += '<span style="color: green">'

            sub_index: int = char_index
            while sub_index < len(code) and code[sub_index] == "R":
                return_string += f"{code[sub_index]}"
                sub_index += 1
                char_index = sub_index - 1

            return_string += "</span>"

        elif code[char_index].isdigit():
            return_string += '<span style="color: orange">'

            sub_index: int = char_index
            while sub_index < len(code) and code[sub_index].isdigit():
                return_string += f"{code[sub_index]}"
                sub_index += 1
                char_index = sub_index - 1

            return_string += "</span>"

        elif code[char_index] == "(" or code[char_index] == ")":
            return_string += code[char_index]

        else:
            raise ValueError(f"highlight: unexpected character {code[char_index]} at position {char_index}.")
        
        char_index += 1
        
    return return_string

###################################################################################################     Kata end     #####################################################################################################






###################################################################################################     Esolang Interpreters #9     #####################################################################################################
                                                                                                  #   RoboScript series 2 - 5 kyu   #
import copy


class Robot:
    def __init__(self, instructions: str) -> None:
        self.instructions: str = instructions
        self.orientation: str = "E"
        self.x_position: int = 0
        self.y_position: int = 0
        self.path: dict[str, list[int]] = {"x_coords" : [], "y_coords" : []} #for simple access to min/max values
        self.path_lst: list[list[int]] = [] #to store the x/y coord pairs
        self.direction_lst: list[str] = [] #to store the direction the movement happened
        self.update_path(x = self.x_position, y = self.y_position)
        self.path_map: str = ""

    def __repr__(self) -> str:
        return f"A robot which is facing {self.orientation}, and its position is ({self.x_position}, {self.y_position})."
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def update_path(self, x: int, y: int) -> None:
        self.path["x_coords"].append(self.x_position)
        self.path["y_coords"].append(self.y_position)

        self.path_lst.append([x, y])
        self.direction_lst.append(self.orientation)
    
    def turn(self, direction: str) -> str:
        if direction == "L":
            if self.orientation == "E":
                self.orientation = "N"
            
            elif self.orientation == "S":
                self.orientation = "E"

            elif self.orientation == "W":
                self.orientation = "S"

            elif self.orientation == "N":
                self.orientation = "W"

        if direction == "R":
            if self.orientation == "E":
                self.orientation = "S"
            
            elif self.orientation == "S":
                self.orientation = "W"

            elif self.orientation == "W":
                self.orientation = "N"

            elif self.orientation == "N":
                self.orientation = "E"

        return f"The robot has turned and now its facing {self.orientation}"
            
    def move(self) -> str:
        if self.orientation == "E":
            self.x_position += 1

        if self.orientation == "W":
            self.x_position -= 1

        if self.orientation == "N":
            self.y_position += 1

        if self.orientation == "S":
            self.y_position -= 1

        self.update_path(x = self.x_position, y = self.y_position)
    
        return f"The robot has moved one grid. It's new position is ({self.x_position}, {self.y_position})."
    

    def map_path(self) -> None:
        wp: dict[str, list[int]] = copy.deepcopy(self.path)
        pl: list[list[int]] = copy.deepcopy(self.path_lst)
        
        #Get min/max values
        x_min: int = min(wp["x_coords"])
        y_min: int = min(wp["y_coords"])

        x_max: int = max(wp["x_coords"])
        y_max: int = max(wp["y_coords"])

        #Create the grid
        ncol: int = x_max - x_min + 1 #the plus 1 is to be inclusive
        nrow: int = y_max - y_min + 1

        grid: list[list[str]] = [[" " for _ in range(ncol)] for _ in range(nrow)]

        #Correct for the positioning by flipping the y-axis (smallest y in bottom, largest in top) and re-centering along the x-axis
        for pair in pl:
            pair[0] = pair[0] - x_min
            pair[1] = y_max - pair[1]

        #Fill the grid using the coordinates the robot touched
        for coord in pl:
            grid[coord[1]][coord[0]] = "*"

        #Convert the grid into a single list of strings (every row is a single string)
        path_lst: list[str] = ["".join(_) for _ in grid]
        
        #Convert the list into a unified string
        path_string: str = "\r\n".join(path_lst)

        self.path_map = path_string


    def execute(self) -> str:
        commands: str = self.instructions
        
        inst_pointer: int = 0
        while inst_pointer < len(commands):
            inst_count: str = ""
            
            if commands[inst_pointer] == "F":
                self.move()

            if commands[inst_pointer] == "L" or commands[inst_pointer] == "R":
                self.turn(direction = commands[inst_pointer])

            if commands[inst_pointer].isnumeric():
                sub_pointer: int = inst_pointer
                print(sub_pointer)
                
                while sub_pointer < len(commands) and commands[sub_pointer].isnumeric():
                    inst_count += commands[sub_pointer]
                    sub_pointer += 1
                
                print(inst_pointer, sub_pointer)

                if commands[inst_pointer - 1] == "F":
                    for _ in range(int(inst_count) - 1):
                        self.move()

                if (commands[inst_pointer - 1] == "L" or commands[inst_pointer - 1] == "R"):
                    for _ in range(int(inst_count) - 1):
                        self.turn(direction = commands[inst_pointer - 1])

                inst_pointer = sub_pointer - 1
                print(inst_pointer)
                
            inst_pointer += 1

        self.map_path()

        
        return self.path_map

###################################################################################################     Kata end     #####################################################################################################

        
       



