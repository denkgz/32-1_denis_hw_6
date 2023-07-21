def bubble_sort(lists):
    for j in range(len(lists) - 1):
        for i in range(len(lists) - 1 - j):
            if lists[i] > lists[i+1]:
                lists[i], lists[i+1] = lists[i+1],lists[i]
    return lists

print('Отсортированный список (Пузырьковый алгоритм): ')
print(bubble_sort([0,20,13,8,3,4]))


def selection_sort(lists2):
    for j in range(len(lists2)-1):
        for i in range(j+1,len(lists2)):
            if lists2[j] > lists2[i]:
                lists2[i],lists2[j] = lists2[j],lists2[i]

    return lists2

print('Отсортированный список (Сортировка выбором) : ')
print(selection_sort([-8,2,10,0,-10]))


def binary_search(Val,A):
    '''N - количество элементов списка A, параметр  А = содержит список с 1 - 5000 элементами'''
    N = len(A)
    ResultOK = False
    First = 0
    Last = N - 1

    while First <= Last:
        Middle = (First + Last) // 2
        if Val == A[Middle]:
            First = Middle
            Last = First
            ResultOK = True
            Pos = Middle
        if Val > A[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1
    if ResultOK == True:
        return f'Элемент найден : Pos - {Pos}'
    else:
        return 'Элемент не найден!'


print(binary_search(Val=50, A=list(range(1,5000+1))))





