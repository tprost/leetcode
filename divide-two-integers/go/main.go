package main

func divide(dividend int, divisor int) int {
	res := divideRecursive(dividend, divisor)

	// truncate the integers to appease the test suite :)
	if res > 2147483647 {
		return 2147483647
	}
	if res < -2147483648 {
		return -2147483648
	}
	return res
}

func divideRecursive(dividend int, divisor int) int {

	// deal with negatives by recursively calling with positives
	if divisor < 0 && dividend < 0 {
		return divideRecursive(-dividend, -divisor)
	}
	if divisor < 0 {
		return -divideRecursive(dividend, -divisor)
	}
	if dividend < 0 {
		return -divideRecursive(-dividend, divisor)
	}
	if dividend == 0 {
		return 0
	}

	// at this point dividend and divisor are both positive
	if divisor == 1 {
		return dividend
	}
	if dividend == divisor {
		return 1
	}
	if divisor > dividend {
		return 0
	}

	i := 0
	for divisor<<(i+1) <= dividend {
		i++
	}
	return 1<<i + divideRecursive(dividend-divisor<<i, divisor)

}
