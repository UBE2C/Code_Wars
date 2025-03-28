
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
            #print(start_stack, end_stack)

            if len(start_stack) > len(end_stack) and sub_code_pointer == len(code): #loop marker mismatch handling
                raise ValueError(f"Unclosed loop-start marker [ found at {start_stack[-1]}. Each open [ marker must have a closing ] marker pair.")
            elif len(start_stack) < len(end_stack) and sub_code_pointer == len(code):
                raise ValueError(f"Uninitiated loop-end marker ] found at {end_stack[0]}. Each open [ marker must have a closing ] marker pair.")

            code_pointer -= 1 #jump back to evaluate the first [ in the next iteration
   
        elif code[code_pointer] == "[" and code_pointer in start_stack: #eval the start of the mapped loop/loops
            if bit_array[tape_pointer] == 0: #if bit array position is 0 jump to loop close
                start_stack_index: int = start_stack.index(code_pointer) # Find the index of the current start marker
                code_pointer = end_stack[-(start_stack_index + 1)] #no -1 offset as we don't eval loop close in the next loop iter step
        
        #elif code[code_pointer] == "]" and code_pointer not in end_stack: #loop marker mismatch handling
            #raise ValueError(f"Uninitiated loop-end marker ] found at {code_pointer}. Each close [ marker must have an opening ] marker pair.")

        elif code[code_pointer] == "]" and code_pointer in end_stack: #eval the end of the mapped loop/loops
            if bit_array[tape_pointer] == 1:  # If current bit is 1, jump back to corresponding start
                end_stack_index: int = end_stack.index(code_pointer)  # Find the index of the current end marker
                code_pointer = start_stack[-(end_stack_index + 1)] - 1
            else:
                # If current bit is 0, exit the current loop
                start_stack.pop()
                end_stack.pop(0)

        code_pointer += 1 #next loop iter, move code pointer
        

    for i in range(len(bit_array)):
        output_string += str(bit_array[i])

    return output_string

###################################################################################################  Kata end  #####################################################################################################
