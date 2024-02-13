import heapq

def merge_k_sorted_arrays(arrays):
    minHeap = []
    result = []
    
    # Add first element of each array to min heap
    for array in arrays:
        heapq.heappush(minHeap, (array[0], array, 0))
        
    # Poll from min heap and add to result  
    # Also add next element from same array
    while minHeap:
        minVal, array, index = heapq.heappop(minHeap)
        result.append(minVal)
        if index+1 < len(array):
            heapq.heappush(minHeap, (array[index+1], array, index+1))
            
    return result