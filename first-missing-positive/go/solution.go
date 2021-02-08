package fmp

func firstMissingPositive(nums []int) int {
	i := 1
	for {
		found := false
		for _, num := range nums {
			if num == i {
				found = true
			}
		}
		if found == false {
			return i
		}
		i++
	}
	return 0
}
