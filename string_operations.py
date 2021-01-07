string = 'Hello World'

print(len(string))
# this will print lenght of characters in string

print(string.index('o'))
# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters 
# away from the first character. Notice how there are actually two o's in the phrase - this method 
# only recognizes the first.

# But why didn't it print out 5? Isn't "o" the fifth character in the string? To make things more 
# simple, Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.
