sum_list = []
for nums in range(1,1001):
    sum_list.append(nums**nums)

print str(sum(sum_list))[-10:]
    