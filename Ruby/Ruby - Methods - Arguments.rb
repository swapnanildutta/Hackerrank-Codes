
def take(arr, slice_length=1)
    len = arr.length
    return [] if slice_length >= len
    arr[-(len - slice_length)..-1]
end
