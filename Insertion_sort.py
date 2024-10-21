def insertion_sort(array):

    for test_sub in range(1,len(array),1):
            sample = array[test_sub]
            compare = test_sub - 1
            while compare >= 0 and sample < array[compare]:
                array[compare + 1] = array[compare]
                compare -= 1
            array[compare+1] = sample
    return array


ins_array = [9,7,6,5,4,2,7,8,9,2,5] + [900]*80000 + list(range(90000,578,-6))
#ins_array = [9]
#ins_array = []
print(insertion_sort(ins_array))






