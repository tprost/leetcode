package main

func canMeasureWater(x int, y int, z int) bool {

	if z == 0 {
		return true
	}

	// make sure x is the bigger jug (if one is bigger than the other)
	if x < y {
		return canMeasureWater(y, x, z)
	}

	if y == 0 && x != z {
		return false
	}

	// if either jug holds one liter, z must be measurable
	if x == 1 || y == 1 {
		return true
	}

	// if neither jug can hold z liters of water, z is not measurable
	if x < z && y < z {
		return false
	}

	// if either jug contains the exact amount we want to measure, z is measurable
	if x == z || y == z {
		return true
	}

	// if you keep emptying the bigger jug into the smaller jug
	// and you eventually get z in the bigger jug
	// then z is measurable
	if (x-z)%y == 0 {
		return true
	}

	// if you keep filling the bigger jug with amounts
	// from the smaller jug
	// and you eventually get z in the bigger jug
	// then z is measurable
	if z%y == 0 {
		return true
	}

	// if you
	// 1. keep emptying the bigger jug into the smaller jug
	//    until it would be empty if you emptied it again into the smaller jug
	// 2. transfer the contents to the smaller jug
	// 3. fill the bigger jug
	// 4. empty bigger jug into smaller jug
	// and the bigger jug contains z then z is measurable
	if x-(y-x%y) == z {
		return true
	}

	// if you
	// 1. keep emptying the smaller jug into the bigger jug
	//    until the bigger jug is full
	// 2. and the smaller jug contains z then z is measurable
	if y-(x%y) == z {
		return true
	}

	return false
}
