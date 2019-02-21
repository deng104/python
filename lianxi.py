# print(["%s+%s=%s"%(x,y,x*y) for y in range(1,x+1) for x in range(1,10) ])
# print("\n".join("\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1, x+1)]) for x in range(1, 10)) )
# print('\n'.join('\t'.join(["%s*%s=%s" %(y,x,x*y) for y in range(1, x+1)]) for x in range(1, 10)))

# def func(a, b=[]):
# 	b.append(a)
# 	return b

# s = func(1)
# print(s)
# s = func(2)
# print(s)

# print("\n".join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


# print("\n".join([
# 	''.join([('Love'[(x-y) % len('Love')]
# 		if ((x*0.05)**2+(y*0.1)**2-1)**3
# -(x*0.05)**2*(y*0.1)**3 <= 0
# 		else ' '
# 		)
# 	for x in range(-30, 30)])
# 	for y in range(30, -30, -1)]
# 	))

lis = [0, 1, 3, 4, 5, 6, 7, 9, 10, 11,12,16,17]

def two_find2(alist, item):
    """二分查找 非递归方式"""
    n = len(alist)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == item:
            return item
        elif item < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

def two_find(alist, item):
    """二分查找 递归方式"""
    n = len(alist)
    if 0 == n:
        return False
    mid = n // 2
    if alist[mid] == item:
        return True
    elif item < alist[mid]:
        return binary_search_2(alist[:mid], item)
    else:
        return binary_search_2(alist[mid + 1:], item)

print(two_find2(lis, 2))
print(two_find(lis, 7))

# def bin_search_rec(data_set, value, low, high):
#       if low <= high:
#           mid = (low + high) // 2
#           if data_set[mid] == value:
#               return mid
#           elif data_set[mid] > value:
#               return bin_search_rec(data_set, value, low, mid - 1)
#           else:
#               return bin_search_rec(data_set, value, mid + 1, high)
#       else:
#           return None

# print(bin_search_rec(4, lis, 0, len(lis))
