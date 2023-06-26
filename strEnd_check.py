def ends_with(str1, str2):

	if str1[len(str1)-1] == str2[len(str2)-1]:
		return True 
	else:
		return False


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

new_str1 = ""
str1_lower = str1.lower()
str2_lower = str2.lower()
for mark in str1_lower:
	if mark == "." or mark == "!" or mark == "?":
		new_str1 += " " + mark 
	else:
		new_str1 += mark 
ls_str1 = new_str1.split()
ls_str2 = str2_lower.split()
print(ends_with(ls_str1, ls_str2))
 