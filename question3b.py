def rearrange_boarding(head, k):
    for i in range(0, len(head), k):
        if i + k <= len(head):
            head[i:i+k] = reversed(head[i:i+k])
        else:
            break
    return head

head1 = [1, 2, 3, 4, 5]
k1 = 2
print(rearrange_boarding(head1, k1)) 

head2 = [1, 2, 3, 4, 5]
k2 = 3
print(rearrange_boarding(head2, k2)) 
