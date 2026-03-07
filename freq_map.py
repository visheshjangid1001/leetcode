def Frequescy_Map(nums):
    freq_map = {}
    for i in range(0,len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]]+=1
        else:
            freq_map[nums[i]]=1
    return freq_map
nums = [1,2,1,2,3,4,5,4,4]
print(Frequescy_Map(nums))