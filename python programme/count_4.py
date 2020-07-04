def count_list(nums):
    count=0
    for num in nums:
        if num==4:
            count=count+1

    return count

print(count_list([1,4,6,7,4,6,4,8,4,9,4,2,4]))
print(count_list([1,4,2,3,6,4,2,8,9,7,4]))
