# Exercises for chapter 2:

# Name: Lisa-Maria Mehta


# ******************
# ** Exercise 2.1 **
# ******************
# A leading '0' indicates that the following int should be read
# in base 8.  A syntax error is generated if any digit 
# following the leading zero is greater than 7.





# ******************
# ** Exercise 2.2 **
# ******************
# Using Python Interpreter
# -----------------------
# >>>  5
# 5
# >>>  x=5
# >>>  x+1
# 6
#
# Using the script
# ----------------
print
print ('Exercise 2.2')
# The following script
print (5)
x = 5
print (x+1)
# generates the following output upon running:
# 5
# 6





# ******************
# ** Exercise 2.3 **
# ******************
# 	Some Easy Math
#	--------------
#		>>> width = 17
#		>>> height = 12
#		>>> delimiter = '.'
#	1.	>>> width/2
#		8
#		>>>
#	2.	>>> width/2.0
#		8.5
#		>>>
#	3.	>>> height/3
#		4
#		>>>
#	4.	>>> 1+2*5
#		11
#		>>>
#	5.	>>> delimiter *5
#		'.....'





# ******************
# ** Exercise 2.4 **
# ******************
#	1.	Volume of Sphere radius = 5 (using interpretter)
#		------------------------------------------------
#			>>> pi = 3.1415926535897932
#			>>> r = 5
#			>>> vol = (4/3)*pi*r**2
#			>>> vol
#			78.53981633974483
#		Volume = 78.54
#
#	2.	Wholesale cost of Book Order (using interpretter)
#		-------------------------------------------------
#			>>> single_price = 24.95
#			>>> number_ordered = 60
#			>>> bookcost = single_price * number_ordered
#			>>> bookcost
#			1497.0
#			>>> discount = 0.4
#			>>> 
#			>>> ship1st = 3
#			>>> shiprest = 0.75
#			>>> shipping = ship1st + (number_ordered -1)*shiprest
#			>>> shipping
#   	    47.25
#			>>> wholesale = bookcost*discount + shipping
#			>>> wholesale
#			731.5500000000001
#		Total cost of order is $731.55
#
#	3a.	What time do I get home? (using interpretter)
#		---------------------------------------------
#			>>> easypace = 8.0 + 15/60.0   		# in min/mile
#			>>> tempopace = 7.0 + 12/60.0		# in min/mile
#			>>> runtime_mins = (1*easypace) + (3*tempopace) + (1*easypace) 
#			>>> runtime_mins      # in minutes
#			38.1
#			>>>
#			>>> starttime = 6 + 52/60.0   #Starttime in hours
#			>>> endtime = startime + runtime_hours
#			>>> endtime_hour
#			7.501666666666667
#		
#			>>> end_hour = endtime_hour - 0.501666666666667
#			>>> end_hour
#			7.0
#			>>> 
#			>>> endtime_mins = (endtime_hour - end_hour) *60
#			>>> endtime_mins 
#			30.100000000000016
#			>>> end_mins = endtime_mins -0.100000000000016
#			>>> end_mins
#			30.0
#			>>>
#			>>> endtime_secs = (endtime_mins- end_mins) *60
#			>>> endtime_secs
#			6.000000000000938
#			>>> end_secs = endtime_secs - 0.000000000000938
#			>>> end_secs
#			6.0
#		I return home at 7:30:06 am.
#		
#	3b.	What time do I get home? using (using script)
#		---------------------------------------------
print
print ('Exercise 2.4.3')
start_hour = 6
start_mins = 52
# Convert starttime to hours with mins as a decimal
starttime = start_hour + start_mins/60.0 
print ('startime ='), start_hour, (':'), start_mins , ('a.m.')

# Equations determning duration of run
easypace = 8.0 + 15/60.0 								# in min/mile
tempopace = 7.0 + 12/60.0								# in min/mile
runtime = (1*easypace) + (3*tempopace) + (1*easypace) 	# in mins
runtime_in_hours = runtime/60	
runtime_mins = int(runtime)
runtime_secs = int((runtime - runtime_mins) * 60) 

print ('runtime ='), runtime_mins, ('minutes and'),
print runtime_secs, ('seconds.')

endtime = starttime + runtime_in_hours				#in hours
endtime_hour = int(endtime)
endtime_mins = int((endtime-endtime_hour)*60)
endtime_secs = int((((endtime - endtime_hour)*60) - endtime_mins) *60)

print
print ('If I start running at'), start_hour, (':'), start_mins,
print ('a.m., I will')
print ('be done by'), endtime_hour ,(':'), endtime_mins,
print ('a.m. and'), endtime_secs, ('seconds.')
