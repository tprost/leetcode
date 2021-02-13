package main

import "testing"

func TestDivideTwoIntegers(t *testing.T) {

	assertDivide := func(t *testing.T, dividend, divisor, expected int) {
		if divide(dividend, divisor) != expected {
			t.Fatalf("expected %v divided by %v to equal %v but got %v", dividend, divisor, expected, divide(dividend, divisor))
		}
	}

	assertDivide(t, 10, 3, 3)

	assertDivide(t, 7, -3, -2)
	assertDivide(t, -7, 3, -2)
	assertDivide(t, -7, -3, 2)

	assertDivide(t, 0, 1, 0)
	assertDivide(t, 1, 1, 1)
	assertDivide(t, 1, -1, -1)
	assertDivide(t, 1, 2, 0)
	assertDivide(t, 1, 10, 0)
	assertDivide(t, 2, 1, 2)
	assertDivide(t, 2, -1, -2)
	assertDivide(t, 2, 2, 1)
	assertDivide(t, 2, 3, 0)
	assertDivide(t, 3, 1, 3)
	assertDivide(t, 3, 2, 1)
	assertDivide(t, 3, 3, 1)
	assertDivide(t, 3, 4, 0)

	assertDivide(t, 4, 1, 4)
	assertDivide(t, 4, 2, 2)
	assertDivide(t, 4, 3, 1)
	assertDivide(t, 4, 4, 1)
	assertDivide(t, 4, 5, 0)

	assertDivide(t, 5, 1, 5)
	assertDivide(t, 5, 2, 2)
	assertDivide(t, 5, 3, 1)
	assertDivide(t, 5, 4, 1)
	assertDivide(t, 5, 5, 1)
	assertDivide(t, 5, 6, 0)

	assertDivide(t, 6, 3, 2)

	assertDivide(t, 16, 2, 8)
	assertDivide(t, 16, 4, 4)
	assertDivide(t, 16, 8, 2)

	assertDivide(t, 32, 8, 4)
	assertDivide(t, 6, 3, 2)
	assertDivide(t, 18, 3, 6)

	assertDivide(t, 1<<31, 2, 1<<30)
	assertDivide(t, 1<<31, 76, 28256363)
	assertDivide(t, -1<<31, 76, -28256363)

	assertDivide(t, -2147483648, -1, 2147483647)
	assertDivide(t, 2147483648, 1, 2147483647)
	assertDivide(t, 2147483648, -1, -2147483648)
	assertDivide(t, -2147483648, 1, -2147483648)

}
