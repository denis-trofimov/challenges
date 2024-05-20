// You are here!
// Your runtime beats 83.75 % of golang submissions.
func intersect(nums1 []int, nums2 []int) []int {
	c1, c2 := make(map[int]int), make(map[int]int)
	var inter []int
	for _, v := range nums1 {
		c1[v] += 1
	}
	for _, v := range nums2 {
		c2[v] += 1
	}
	for k, v1 := range c1 {
		if v2, ok := c2[k]; ok {
			for i := 0; i < v1 && i < v2; i++ {
				inter = append(inter, k)
			}
		}
	}
	return inter
}