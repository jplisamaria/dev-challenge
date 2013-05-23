# Exercises for chapter 3:

# Name: Lisa-Maria Mehta


# ******************
# ** Exercise 3.1 **
# ******************
# Calling a function before it's been defined
# -------------------------------------------
#
#repeat_lyrics()
#
#def print_lyrics():
#	print "I'm a lumberjack, and I'm OK."
#	print "I sleep all night and I work all day."
#
#def repeat_lyrics():
#	print_lyrics()
#	print_lyrics()
#
#
# Placing the repeat_lyrics() function call at the beginning
# yields the following error:
#		Traceback (most recent call last):
#		  File "chapter3_exercises.py", line 9, in <module>
#		    repeat_lyrics()
#		NameError: name 'repeat_lyrics' is not defined





# ******************
# ** Exercise 3.2 **
# ******************
# Changing order of function definitions
# --------------------------------------
print
print ('Exercise 3.2')

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm OK."
	print "I sleep all night and I work all day."

repeat_lyrics()
# Changing the order of the function definitions has no apparent
# negative effect on the execution of the program.





# ******************
# ** Exercise 3.3 **
# ******************
# Right Justify
# -------------
print
print ('Exercise 3.3')
word = ('allen')
x = len(word)
print ('.')*70   #as a visual aid to determine line length
space = (' ')*(70-x)
cat = space + word
print cat
print





# ******************
# ** Exercise 3.4 **
# ******************
# Using function objects
# ----------------------
#	1.	Typing and testing script
#		-------------------------
print ('Exercise 3.4.1')

def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)	


#	2.	Passing two arguments
#       ---------------------
print
print ('Exercise 3.4.2')

def do_twice2(f2, word):
	f2(word)
	f2(word)

def print_spam2(word):
	print word

do_twice2(print_spam2, 'spam2')

#	3.	General print_twice function
#       ----------------------------
print
print ('Exercise 3.4.3')

def do_twice3(f3):
	f3()
	f3()

def print_twice3():
	print 'spam3'
	print 'spam3'

do_twice3(print_twice3)


#	4.	Passing two arguments with print_twice function
#       -----------------------------------------------
print
print ('Exercise 3.4.4')

def do_twice4(f4, word4):
	f4(word4)
	f4(word4)

def print_twice4(word4):
	print word4
	print word4

do_twice4(print_twice4, 'spam4')


#	.	do_four function
#       ----------------
print
print ('Exercise 3.4.5')

def do_twice5(f5, word5):
	f5(word5)
	f5(word5)

def do_four(do_twice5, word5):
	do_twice5 (word5)
	do_twice5 (word5)

def print_twice5(word5):
	print word5
	print word5

do_four(print_twice5, 'spam5')