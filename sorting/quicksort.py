
def sort(array=[12,4,5,6,7,3,1,15]):
    """
    Sort the array by using quicksort
    average O(nlogn), worst case O(n^2)
    """

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        # this choice of pivot causes worst-case behavior in sorted lists
        # better choice is median of first,last,middle elements (Sedgewick)
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array



a = [5,3,16,4,5,7,8,9,10,2,42,34,55,1]

print(a)

b = sort(a)

print(b)
