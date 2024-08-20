import string

from cupshelpers.ppds import normalize


def palindrome(my_string):
    for search in range(0, len(my_string), 1):
        if my_string.lower()[search] == my_string.lower()[-1 - search]:
            continue
        else:
            return "Given string is not a palindrome."
            break
    else:
        return "Given string is a palindrome."

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def CountFreq(my_string,char_freq):
    freq = 0
    my_string = my_string.lower()
    for i in range(len(my_string)):
        if my_string[i]==char_freq:
            freq+=1
            
    return freq

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def longest_word(my_string):
    start_pos = end_pos = length_holder = 0           #VERY FEW FUCNTION CALLS AND FASTER THAN USUAL CODE
    equal_holder = []
    for iter in range(0, len(my_string), 1):
        if my_string[iter] == ' ':
            if (iter - end_pos) > length_holder:
                equal_holder.clear()
                length_holder = (iter - end_pos)
                end_pos = iter + 1
                start_pos = end_pos - 1

            elif (iter - end_pos) == length_holder:
                length_holder = (iter - end_pos)
                end_pos = iter + 1
                start_pos = end_pos - 1
                equal_holder.append(start_pos)

            else:
                end_pos = iter + 1

    if (iter + 1) - end_pos > length_holder:
        print('Longest word is -',my_string[end_pos: iter + 1])
    else:
        compress = []
        for measure in equal_holder:
            compress.append(my_string[measure - length_holder: measure])
            #print('longest words are -',my_string[start_pos - length_holder: start_pos])
        print("Longest words are - ",set(compress))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def first_index(my_string, sub_string):
    my_string = my_string.lower()                  #FOUR TIMES FASTER THAN USUAL CODE
    sub_string = sub_string.lower()
    len_of_substr = len(sub_string)
    len_of_mystr = len(my_string)

    for search in range(0, len_of_mystr - len_of_substr + 1, 1):
        if my_string[search] == sub_string[0]:
            for sub_search in range(1, len_of_substr, 1):
                if sub_string[sub_search] == my_string[search + sub_search]:
                    continue
                else:
                    break
            else:
                return search
            continue
        else:
            continue
    return "Substring not found"


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def occurence(my_string):
    my_string = my_string+" "
    current_word = ''
    process_list = []
    my_string = my_string.lower()
    for collector in range(0,len(my_string),1):
        if my_string[collector] != " ":
            current_word += my_string[collector]
        else:
            process_list.append(current_word)
            current_word = ''
    process_set =  set(process_list)
    final_count_list = []
    for word in process_set:
        count_word = 0
        for check in range(0,len(process_list),1):
            if word==process_list[check]:
                count_word+=1
        final_count_list.append((word,count_word))
    return final_count_list


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def menu():
    print("Enter 1 to for palindrome. \nEnter 2 to check for longest word. \nEnter 3 for index of first occurence of a subtring. \nEnter 4 knowing occurrence of each word.\nEnter 5 to check how many times a character appeared in a string.")

test_str = input("Enter the string - ")
check = True
while(check and len(test_str)!=0):
    menu()
    choice = int(input("Enter choice - "))

    while 5 < choice or choice < 1:
        print("Enter a valid choice!!!")
        choice = int(input("Enter choice - "))

    if choice==1:
  
        print(palindrome(test_str))
    
    elif choice==2:
        longest_word(test_str)
        
    elif choice==3:
        substr = input("Enter the substring - ")
        print(first_index(test_str,substr))
        
    elif choice==4:
        print(occurence(test_str))

        
    else:
        charac = input("Enter the character - ")
        print(CountFreq(test_str,charac))

    want = input("Want to continue ? if yes type yes otherwise no\n --- ")
    while(want.lower()!="yes" and want.lower()!="no"):
        print("Enter yes or no only")
        want = input("Want to continue ? if yes type yes otherwise no\n --- ")
    if want.lower()=="no":
        print("Thank you for using our program!")
        check = False    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
