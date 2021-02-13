package main

func flip(number int) int {
	return -number
}

func divide(dividend int, divisor int) int {

	// deal with negatives by recursively calling with positives
	if divisor < 0 && dividend < 0 {
		return divide(-dividend, -divisor)
	}
	if divisor < 0 {
		return -divide(dividend, -divisor)
	}
	if dividend < 0 {
		return -divide(-dividend, divisor)
	}

	// at this point dividend and divisor are both non-negative
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
	return 1<<i + divide(dividend-divisor<<i, divisor)

}
