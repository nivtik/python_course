my_list=list(range(1,13))

def list_slicer(my_list):
    slice_length=int(len(my_list)/2)
    l1=my_list[0:slice_length+1]
    l2=my_list[slice_length+1:]
    print(l1,l2)
    return l1,l2

l1,l2=list_slicer(my_list)