// Your runtime beats 18.15 % of golang submissions.

func containsDuplicate(nums []int) bool {
	c := make(map[int]int)
	for _, n := range nums {
		c[n] += 1
	}
	for _, f := range c {
		if f > 1 {
			return true
		}
	}
	return false
}

// Your runtime beats 86.90 % of golang submissions.
func containsDuplicate(nums []int) bool {
	c := make(map[int]bool)
	var ok bool
	for _, n := range nums {
		_, ok = c[n]
		if ok {
			return true
		}
		c[n] = true
	}
	return false
}