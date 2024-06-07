l = [1,2,3,4,5,6,7,8,9,10]
turned_list = l[1:]
print(l)
turned_list_final = [l[0]]
turned_list_final.extend(turned_list[-1:] + turned_list[:-1])
print(turned_list_final)