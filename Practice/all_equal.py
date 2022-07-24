def all_equal(list1):
    for i in (0, len(list1) - 2):
        print(i)
        if list1[i] != list1[i + 1]:
            return False

    return True


k=all_equal([1,2,1,1,1])
print(k)