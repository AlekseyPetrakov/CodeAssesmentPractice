def kFrequent(k,nums) -> int:
    currentCount = 0
    for i in range(len(nums)):
        if i == 0: #base case (if first number then current count will just be 1)
            currentCount = 1
        elif nums[i] == nums[i-1]:
            currentCount = currentCount + 1
            if currentCount == k: # If we are able to find this number, then we return it and break
                print(nums[i])
                break
        else:
            currentCount = 1
    print(currentCount)

# Required input like nums = [3,4,5,2,3,2,5,5,5,6,2], as well as an integer like k = 3
#kFrequent(2,nums)
