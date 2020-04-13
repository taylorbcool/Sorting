# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc)
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[smallest_index]:
        smallest_index = j

    # TO-DO: swap
    arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

  return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  # iterate over array
  for i in range(0, len(arr) - 1):
    # need to know if items have been swapped to know if any work needs to be done
    swap = False

    # iterate again and swap values if needed
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swap = True

    # print to see if it's working
    print(arr)

  # if no swaps happened, we should be done
    if swap == False:
      return arr

  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
  

  return arr