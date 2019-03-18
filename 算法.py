li = [7,5,4,6,3,8,2,9,1]
 
# 冒泡排序
# 时间复杂度: O(n^2)
# 空间复杂度: O(1)
def BubbleSort(li):
	for i in range(len(li)-1):
		exchange = False
		for y in range(len(li)-i-1):
			if  li[y]>li[y+1]:
				li[y], li[y+1] = li[y+1], li[y]
				ecxhange = True
		if not exchange:
			return
# BubbleSort(li)
# print(li)

# 选择排序
# 时间复杂度: O(n^2)
# 空间复杂度: O(1)
def SelectSort(li):
	for i in range(len(li)-1):
		min_loc = i
		for j in range(i+1, len(li)):
			if li[j] < li[min_loc]:
				min_loc = j
		if min_loc != i:
			li[i], li[min_loc] = li[min_loc], li[i]
# SelectSort(li)
# print(li)

# 插入排序
# 时间复杂度: O(n^2)
# 空间复杂度: O(1)
def InsertSort(li):
	for i in range(1, len(li)):
		tmp = li[i]
		j = i- 1
		while j >= 0 and tmp < li[j]:
			li[j + 1] = li[j]
			j = j - 1
		li[j + 1] = tmp
# InsertSort(li)
# print(li)

# 快速排序
# 时间复杂度: O(nlogn)
# 空间复杂度: O(1)
def partition(li, left, right):
	tmp = li[left]
	while left < right:
		while left < right and li[right] >= tmp:
			right -= 1
		li[left] = li[right]
		while left < right and li[left] <= tmp:
			left += 1
		li[right] = li[left]
	li[left] = tmp
	return left


def QuickSort(li, left, right):
	if left < right:
		mid = partition(li, left, right)
		QuickSort(li, left, mid-1)
		QuickSort(li, mid+1, right)
QuickSort(li, 0, len(li)-1)
print(li)
