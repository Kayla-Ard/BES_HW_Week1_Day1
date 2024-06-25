# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "lets_go_team" gets converted to "letsGoTeam"

def solution(s):
    camel_case = ""
    capitalize_next = False
    
    for char in s:
        if char == '-' or char == '_':
            capitalize_next = True
        else:
            if capitalize_next:
                camel_case += char.upper()
                capitalize_next = False
            else:
                camel_case += char
    
    return camel_case