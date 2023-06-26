def starts_with(str1, str2):
	if str1[0] == str2[0]:
		return True 
	else:
		return False


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
str1_lower = str1.lower()
str2_lower = str2.lower()
ls_str1 = str1_lower.replace(",","").split()
ls_str2 = str2_lower.split()
print(starts_with(ls_str1, ls_str2))
 