package graycode

import "math"

func powInt(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func grayCode(n int) []int {
	if n <= 0 {
		return []int{}
	}
	if n == 1 {
		return []int{0, 1}
	}
	result := grayCode(n - 1)
	for i := len(result) - 1; i >= 0; i-- {
		result = append(result, powInt(2, n-1)+result[i])
	}
	return result

}
