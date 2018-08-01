def merge_sort(array):
    if len(array) <=1 :

        return array

    midpoint = int(len(array)/2)
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left,right)

def merge(left,right):
    result=[]
    L_pointer = R_pointer = 0
    while L_pointer < len(left) and R_pointer < len(right):
        if left[L_pointer] < right[R_pointer]:
            result.append(left[L_pointer])
            L_pointer+=1

        else:

            result.append(right[R_pointer])
            R_pointer +=1

    result.extend(left[L_pointer:])
    result.extend(right[R_pointer:])

    return result


def main():
    array = [1,2,3,4,5,2,100,34,56,12,-90,89,9]
    print(array)

    result = merge_sort(array)
    print(result)

if __name__ == "__main__":

   main()