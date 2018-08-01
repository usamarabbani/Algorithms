# Assuming -1 is filled
# for the places where element
# is not available

NA = -1


# Function to move m elements
# at the end of array mPlusN[] 
def moveToEnd(mPlusN, size):
    i = 0
    j = size - 1
    for i in range(size - 1, -1, -1):
        if (mPlusN[i] != NA):
            mPlusN[j] = mPlusN[i]
            j -= 1


# Merges array N[]
# of size n into array mPlusN[]
# of size m+n
def merge(mPlusN, N, m, n):
    i = n  # Current index of i/p part of mPlusN[]
    j = 0  # Current index of N[]
    k = 0  # Current index of of output mPlusN[]
    while (k < (m + n)):

        # Take an element from mPlusN[] if
        # a) value of the picked
        # element is smaller and we have
        # not reached end of it
        # b) We have reached end of N[] */
        if ((i < (m + n) and mPlusN[i] <= N[j]) or (j == n)):

            mPlusN[k] = mPlusN[i]
            k += 1
            i += 1

        else:  # Otherwise take element from N[]

            mPlusN[k] = N[j]
            k += 1
            j += 1


# Utility that prints
# out an array on a line 
def printArray(arr, size):
    for i in range(size):
        print(arr[i], " ", end="")

    print()


# Driver function to
# test above functions 

# Initialize arrays
mPlusN = [2, NA, 13, 15, 20, NA, NA, NA,]
N = [5, 7, 9, 25]
n = len(N)

m = len(mPlusN) - n

# Move the m elements
# at the end of mPlusN
moveToEnd(mPlusN, m + n)

# Merge N[] into mPlusN[] 
merge(mPlusN, N, m, n)

# Print the resultant mPlusN 
printArray(mPlusN, m + n)

