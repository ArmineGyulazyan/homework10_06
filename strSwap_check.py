def swap_strings(str1, str2):
	temp = str1
	str1 = str2
	str2 = temp

	print(str1 + " \n" + str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
swap_strings(str1, str2)