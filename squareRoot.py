'''take user input
number = int(input("Enter a number to find the square root : "))
#end case where user enter less than 0 number
if number < 0 :
  print("Please enter a valid number.")
else :

  sq_root = number ** 0.5

  print("Square root of {} is {} ".format(number,sq_root))'''


def floorSqrt(x):
    # Base cases
    if x<0:
        return "Please enter a positive number"

    if (x == 0 or x == 1):
        return x

    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = x
    while (start <= end):
        mid = (start + end) // 2

        # If x is a perfect square
        if (mid * mid == x):
            return mid

        # Since we need floor, we update
        # answer when mid*mid is smaller
        # than x, and move closer to sqrt(x)
        if (mid * mid < x):
            start = mid + 1
            ans = mid

        else:

            # If mid*mid is greater than x
            end = mid - 1

    return ans


# driver code
x = 9
print(floorSqrt(x))






