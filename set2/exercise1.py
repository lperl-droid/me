"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]

# prints each item of the list on a new line
for word in some_words:
    print(word)

# prints each item of the list on a new line
for x in some_words:
    print(x)

# print some_words as a list on one line
print(some_words)

#if the length of some_words is >3, let the user know it has more than 3 words
if len(some_words) > 3:
    print("some_words contains more than 3 words")

# print the system, node, release, version, date in UTC and the CPU 
# of the user
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
