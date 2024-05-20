func removeDuplicates(nums []int) int {
    j := 0
    for i:=1; i < len(nums); i++ {
        if nums[j] != nums[i] {
            j += 1
            if i != j {
                nums[j] = nums[i]
            }
        }
    }
    return j+1
}

// You are here!
// Your runtime beats 85.83 % of golang submissions.
