package main

import "testing"

func TestWaterAndJug(t *testing.T) {

	assertCanMeasureWater := func(t *testing.T, x, y, z int) {
		if !canMeasureWater(x, y, z) {
			t.Fatalf("expected %v to be measurable with jugs %v and %v", z, x, y)
		}
		if !canMeasureWater(y, x, z) {
			t.Fatalf("expected %v to be measurable with jugs %v and %v", z, y, x)
		}
	}

	assertCannotMeasureWater := func(t *testing.T, x, y, z int) {
		if canMeasureWater(x, y, z) {
			t.Fatalf("expected %v to NOT be measurable with jugs %v and %v", z, x, y)
		}
		if canMeasureWater(y, x, z) {
			t.Fatalf("expected %v to NOT be measurable with jugs %v and %v", z, y, x)
		}
	}

	assertCannotMeasureWater(t, 2, 6, 5)
	assertCanMeasureWater(t, 1, 1, 1)
	assertCanMeasureWater(t, 9, 9, 9)
	assertCanMeasureWater(t, 12, 9, 9)

	assertCanMeasureWater(t, 15, 9, 6)
	assertCanMeasureWater(t, 17, 11, 6)
	assertCanMeasureWater(t, 9, 15, 6)
	assertCanMeasureWater(t, 11, 17, 6)

	assertCanMeasureWater(t, 15, 1, 5)
	assertCanMeasureWater(t, 11, 1, 5)
	assertCanMeasureWater(t, 1, 21, 5)
	assertCanMeasureWater(t, 1, 456, 5)

	assertCanMeasureWater(t, 3, 5, 4)
	assertCanMeasureWater(t, 6, 10, 8)
	assertCanMeasureWater(t, 9, 15, 12)

	assertCanMeasureWater(t, 3, 5, 1)
	assertCanMeasureWater(t, 6, 10, 2)
	assertCanMeasureWater(t, 9, 15, 3)

	assertCanMeasureWater(t, 3, 11, 2)

	assertCanMeasureWater(t, 3, 11, 1)

	assertCanMeasureWater(t, 45, 52, 7)
	assertCanMeasureWater(t, 73, 16, 9)

	assertCanMeasureWater(t, 73, 16, 66)
	assertCanMeasureWater(t, 73*2, 16*2, 66*2)
	assertCanMeasureWater(t, 73*3, 16*3, 66*3)

	assertCanMeasureWater(t, 56, 7, 21)

	assertCanMeasureWater(t, 1000000, 10, 160)
	assertCannotMeasureWater(t, 1000000, 10, 11)

	assertCanMeasureWater(t, 0, 3, 3)
	assertCannotMeasureWater(t, 0, 3, 2)
	assertCanMeasureWater(t, 2, 3, 0)
	assertCanMeasureWater(t, 2, 0, 0)

	assertCanMeasureWater(t, 4, 6, 8)

}
