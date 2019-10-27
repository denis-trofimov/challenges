

func plusOne(d []int) []int {
	mind, plus := 0, 1
	for i := len(d) - 1; i >= 0; i-- {
		if d[i]+plus > 9 {
			mind = (d[i] + plus) / 10
			d[i] = (d[i] + plus) % 10
			plus = mind
		} else {
			d[i] += plus
			plus = 0
			break
		}
	}
	if plus > 0 {
		n := make([]int, len(d)+1)
		n[0] = plus
		for i, v := range d {
			n[i+1] = v
		}
		return n
	}
	return d
}