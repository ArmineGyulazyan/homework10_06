def find_last_not_of(str_check,sequence):
	count = " "
	str_ch = str_check.lower()
	sequence_ch = sequence.lower()
	for i in str_ch[::-1]:
		if sequence_ch.find(i) < 0:
			count = i
			break
			
		
	print(count)						


sample_str = input("Enter the string: ")
sample_sequence = input("Enter the sequence: ")
find_last_not_of(sample_str,sample_sequence)