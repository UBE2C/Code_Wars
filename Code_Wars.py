
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


# Trying to differentiate floats and ints
test_year = 1604

per_hundred_remainder = test_year % 100

if test_year % 100 == 0:
    print("This is not a leap year")

elif test_year % 400  == 0 and test_year % 4 == 0:
    print("This is a leap year.")

else:
    print("This is not a leap year")



year = 1600



def is_leap_year(year):
    if year % 100 == 0:
        return False

    elif year % 400  == 0 or year % 4 == 0:
        return True

    else:
        return False

is_leap_year(year = 1600)



















