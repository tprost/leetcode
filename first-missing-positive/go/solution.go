package fmp

func firstMissingPositive(nums []int) int {

	min := nums[0]

	for _, num := range nums {
		if num > 0 {
			if min <= 0 || num < min {
				min = num
			}
		}
	}

	if min <= 0 {
		return 1
	}

	if min > 1 {
		return 1
	}

	i := 0
	for i < len(nums) {
		for nums[i] > 0 && nums[i] <= len(nums) && nums[i] != i+1 {
			temp := nums[nums[i]-1]
			nums[nums[i]-1] = nums[i]
			nums[i] = temp
		}
		i++
	}

	for i := 0; i < len(nums); i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}

	return len(nums) + 1

}
