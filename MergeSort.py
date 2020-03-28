def merge(a,b):
    c = []
    h = j = 0
    while h < len(a) and j < len(b):
        '''
        1.先判断分割开的序列的第一个数值，小的加到新序列中，然后索引自增1
        2.循环执行1，直到有一方序列全部放在c中，再去判断是哪一方先排序完，对未排序完的序列进行遍历，新增到c中，最后返回已排序的列表c
        '''
        if a[h] < b[j]:
            c.append(a[h])
            h += 1
        else:
            c.append(b[j])
            j += 1
    if h == len(a):
        for i in b[j:]:
            c.append(i)
    else:
        for i in a[h:]:
            c.append(i)
    return c

def merge_sort(lists):
    '''
    利用递归，对数列进行分割，直到分割成单个数字为止
    先判断列表长度，如果列表长度小于等于1，直接返回列表本身；若大于1，则需要进行分割
    '''
    if len(lists) <= 1:
        return lists
    else:
        middle = len(lists) // 2
        left = lists[:middle]
        right = lists[middle:]
        a = merge_sort(left)
        b = merge_sort(right)
        return merge(a,b)

if __name__ == '__main__':
    l = [6,4,7,2,3,5,1]
    print(merge_sort(l))
