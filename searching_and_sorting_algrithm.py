# 遍历：O(len())，不需要排序
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

# 线性复杂度：O(n)，需要排序
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# 二分法：O(Log(n))，需要排序，排序的时间复杂度就已经是O(n)了，
# 也就是说先排序再二分法，就比上面的效率低了
# 在越多次执行本列表中元素比较大小的情况下，只排序一次是值得的
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

# 冒泡排序，O(n**2)——所有排序时间复杂度都是二次的O(n**2)
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

# 合并排序，O(n*log(n)) where n is len(L)
# 分解列表成只有L[0]和L[1]的最小列表，之后逐级合并
# 为什么效率更高：当其中一个表没有数据的时候，copy剩下的元素放到return列表后就OK
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
# 合并排序——递归方式
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
    return merge(left, right)
