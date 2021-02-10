package graycode

import "testing"
import "fmt"

func assertLength(t *testing.T, sequence []int, length int) {
	if len(sequence) != length {
		t.Fatalf("expected sequence to be of length %v but it was %v", length, len(sequence))
	}
}

func assertRange(t *testing.T, sequence []int, min, max int) {
	for i := range sequence {
		if sequence[i] < min {
			t.Fatalf("sequence %v contained number less than %v", sequence, min)
		}
		if sequence[i] > max {
			t.Fatalf("sequence %v contained number greater than %v", sequence, max)
		}
	}
}

func assertNoDuplicates(t *testing.T, sequence []int) {
	for i := range sequence {
		for j := range sequence {
			if i != j && sequence[i] == sequence[j] {
				t.Fatalf("sequence %v contained duplicate", sequence)
			}
		}
	}
}

func differByOneBit(a, b int) bool {
	if a^b > 0 {
		for i := 0; i < 32; i++ {
			if a^b == powInt(2, i) {
				return true
			}
		}
	}
	return false
}

func assertGray(t *testing.T, sequence []int) {
	for i := range sequence {
		if i == 0 {
			continue
		}
		previous := sequence[i-1]
		current := sequence[i]
		if !differByOneBit(previous, current) {
			t.Fatalf("sequence %v is not gray: %v and %v", sequence, previous, current)
		}
	}
}

func TestSolution(t *testing.T) {

	for i := 1; i <= 16; i++ {
		t.Run(fmt.Sprintf("GrayCode%v", i), func(t *testing.T) {

			sequence := grayCode(i)

			// check length
			assertLength(t, sequence, powInt(2, i))

			// check each number is within expected range
			assertRange(t, sequence, 0, powInt(2, i)-1)

			// check for duplicates
			assertNoDuplicates(t, sequence)
			assertGray(t, sequence)

		})
	}

}
