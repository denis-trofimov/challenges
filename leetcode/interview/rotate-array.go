// You are here!
// Your runtime beats 98.61 % of golang submissions
func rotate(nums []int, k int) {

	l := len(nums)
	k = k % l
	if k == 0 {
		return
	}
	head := make([]int, k)
	for i := 0; i < k; i++ {
		head[i] = nums[l-k+i]
	}
	for i := l - k - 1; i >= 0; i-- {
		nums[i+k] = nums[i]
	}
	for i := 0; i < k; i++ {
		nums[i] = head[i]
	}
}