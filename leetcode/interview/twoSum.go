package main

import "fmt"

// You are here!
// Your runtime beats 94.80 % of golang submissions.
func twoSum(nums []int, target int) []int {
	pair := make([]int, 2)
	index := make(map[int]int)
	for i, v := range nums {
		if v == target/2 && target%2 == 0 {
			if pair[0] == 0 {
				pair[0] = i + 1
			} else {
				pair[1] = i + 1
			}
		} else {
			index[v] = i
		}
	}

	if target%2 == 0 && pair[0] != 0 && pair[1] != 0 {
		pair[0] -= 1
		pair[1] -= 1
		return pair
	}
	var j int
	var ok bool
	for k, i := range index {
		j, ok = index[target-k]
		if ok {
			pair[0] = i
			pair[1] = j
			break
		}
	}
	return pair
}

func main() {
	a := []int{3, 2, 4}
	t := 6
	r := twoSum(a, t)
	fmt.Println(r)
}
