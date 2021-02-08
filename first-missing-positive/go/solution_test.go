package fmp

import "testing"

func assertFirstMissingPositive(t *testing.T, sequence []int, expected int) {
	fmp := firstMissingPositive(sequence)
	if fmp != expected {
		t.Fatalf("expected first missing positive to be %v but got %v", expected, fmp)
	}
}

func TestFirstMissingPositive(t *testing.T) {

	t.Run("StupidCase", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{}, 1)
	})

	t.Run("AllNegative", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{-1, -2, -3}, 1)
	})

	t.Run("AllNegativeOnePositive", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{-1, 5, -2, -3}, 1)
	})

	t.Run("AllPositiveButNo1", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{7, 5, 3, 2}, 1)
	})

	t.Run("Example1", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{1, 2, 0}, 3)
	})

	t.Run("Example2", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{3, 4, -1, 1}, 2)
	})

	t.Run("Example3", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{7, 8, 9, 11, 12}, 1)
	})

	t.Run("Other", func(t *testing.T) {
		assertFirstMissingPositive(t, []int{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}, 11)
		assertFirstMissingPositive(t, []int{10, 9, 8, 6, 5, 4, 3, 2, 1}, 7)
		assertFirstMissingPositive(t, []int{10, 19, 8, 6, 5, 4, 3, 2, 29}, 1)
	})

	t.Run("300", func(t *testing.T) {
		sequence := []int{}
		for i := 300; len(sequence) < 300; i-- {
			sequence = append(sequence, i)
		}
		assertFirstMissingPositive(t, sequence, 301)
	})

}
