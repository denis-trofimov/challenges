// You are here!
// Your runtime beats 95.50 % of golang submissions
func singleNumber(nums []int) int {
	s := 0
	for _, n := range nums {
		s ^= n
	}
	return s
}