#二分查找：
#先拿出中间的数mid,输入比较
#如果比mid大，就在后面的一半的数组 继续折半查找
#如果比mid小，就在前面的数组，折半查找

lst = [1,3,7,10,22,299,1000,2000,30000,40000]
find_to_num = int(input('input a num:'))
start = 0
end = len(lst) - 1
while True:
    mid = (start + end) // 2
    mid_num = lst[mid]
    if find_to_num < mid_num:
        end = mid
    elif find_to_num > mid_num:
        start = mid
    else:
        print('find',mid)
        break