# Question 1A
import heapq

def most_utilized_classroom(n, classes):

    classes.sort(key=lambda x: (x[0], -x[1]))
    
    rooms_heap = [(0, i) for i in range(n)]  
    heapq.heapify(rooms_heap)
    
   
    class_count = [0] * n
    
   
    for start_time, end_time in classes:
        
        if rooms_heap[0][0] <= start_time:  
            room_end_time, room_number = heapq.heappop(rooms_heap)
        else:  
            room_end_time, room_number = heapq.heappop(rooms_heap)
            start_time = room_end_time  
        
        
        heapq.heappush(rooms_heap, (start_time + (end_time - start_time), room_number))
        class_count[room_number] += 1
    
    
    max_classes = max(class_count)
    return class_count.index(max_classes)


print(most_utilized_classroom(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))  
print(most_utilized_classroom(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))  
