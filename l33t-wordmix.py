#subs is a dictionary type, relates a character to a list of possible substitutions
#this is a global for now, just so it's not in the way, could be passed as a parameter
#important: any string with special characters needs to be escaped, adding a backslash
subs = { "A" : ['4', '/-\\', '@', '^', '/\\' , 'a'],
         "B" : ['8', '13', 'b'],
         "C" : ['(', '{' , '[[', '<', 'c'],
         "D" : [')', '[}', 'd'],
         "E" : ['3', 'ii', 'e'],
         "F" : ['|=','(=', 'ph', 'f'],
         "G" : ['6', '9', '&','g'],
         "H" : ['#', '|-|', '(-)', 'h'],
         "I" : ['1', '!', '|', 'i'],
         "J" : [';' , 'j'],
         "K" : ['|<', '|{', ']<', ']<', 'k'],
         "L" : ['|','1', '|_', 'l'],
         "M" : ['^^','JVL', 'm'],
         "N" : ['n'],
         "O" : ['0', '()', 'o'],
         "P" : ['p'],
         "Q" : ['(,)', '0', 'O', 'q'],
         "R" : ['|2', '|?', '?', 'r'],
         "S" : ['5','$', 's'],
         "T" : ['7', '+', 't'],
         "U" : ['(_)', '|_|', 'u'],
         "V" : ['^' , 'v'],
         "W" : ['VV', '///' , 'w'],
         "X" : ['><' , 'x'],
         "Y" : ['y'],
         "Z" : ['2', 'z'] }



#function takes a string, returns all single letter subsitutions according to sub rules above
def enum_mod_pass(password):
    #results list will hold each new password generated
    results = []

    #iterate over each letter in original password where i is the index of the letter
    #using index rather than "for i in password" because we need the index, not just the value
    for i in range(len(password)):
        #store list of possible substitutions
        #using password.upper() because keys in subs are uppercase
        #lowercase wouldn't return anything
        possible_letter_subs = subs[password.upper()[i]];
        #iterate over each possible character substitution
        for j in possible_letter_subs:
            #arr holds the list representation of original password
            arr = list(password)
            #change the letter at the current index to that of the current substitution
            arr[i] = j
            #convert array back into a string by joining each letter using no separator ('')
            subd_pass = ''.join(arr)
            #add this string to the final list of possible passwords
            results.append(subd_pass)

    #return the final list from this function
    return results

def main():
    usrWord = raw_input('Enter your base password: ')
    print enum_mod_pass(usrWord)

if __name__ == "__main__":
    main()
    
