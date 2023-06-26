def rotate_by(origin_list, num):

	need_index = len(origin_list) - num
	first_temp = origin_list[:need_index]
	last_temp = origin_list[need_index:len(origin_list)]
	first_temp.reverse()
	last_temp.reverse()
	new_list = first_temp + last_temp
	new_list.reverse()
	print(new_list)

origin_list = [1,2,3,4,5,6,7]
num = 2
rotate_by(origin_list, num)

