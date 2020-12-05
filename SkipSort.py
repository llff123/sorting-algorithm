def skip_sort(list,start,end):
    '''
    接收一个列表和第一个索引以及最后一个索引
    1.将列表的第一个值定位第一次循环的基准值，大于基准值的排在右边，小于基准值的排在左边
    2.先从右开始往左遍历，直到找到一个小于基准值的，将其赋值给此时的左索引下的值
    3.再从左开始往右遍历，直到找到一个大于基准值的，将其赋值给此时的右索引下的值
    4.如此循环，直到左指针大于等于右指针时，循环终止，此时的值成为新基准值
    5.迭代循环
    '''
    if start >= end:
        return
    low = start
    high = end
    mid = list[start]
    while low < high:
        while low < high and list[high] >= mid:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] <mid:
            low += 1
        list[high] = list[low]
    list[low] = mid
    skip_sort(list,0,low-1)
    skip_sort(list,low+1,end)

if __name__ == '__main__':
    list = [4,4,435,6,2,5,73,4,7,9,3,1,2]
    skip_sort(list,0,len(list)-1)
    print(list)
