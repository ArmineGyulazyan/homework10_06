def convert_to_int(str_check):

	try:
		fl_str = float(str_check)
		int_str = int(fl_str) 
		print("The integer representation is ", int_str)			

	except ValueError:	
			print(str + " Cannot be converted to integer")

convert_str = input("Enter the string: ")
convert_to_int(convert_str) 
