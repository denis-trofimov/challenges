// You are here!
// Your runtime beats 98.32 % of golang submissions.
func moveZeroes(nums []int)  {
    i,j := 0, 0
    l := len(nums)
    for ;i<l && j<l; i++ {
        if nums[i] == 0 {
            if i+1 > j {
                j = i+1
            }
            for ; j<l; j++ {
                if nums[j] != 0 {
                    nums[i] = nums[j]
                    nums[j] = 0
                    j++
                    break
                }
            }
        }   
    }
}
