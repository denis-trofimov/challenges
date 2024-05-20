package main

func reverse(x int) int {
	r := 0
	for x != 0 {
		r = r*10 + x%10
		x /= 10
	}
	if r > 2147483647 || r < -2147483648 {
		return 0
	}
	return r
}

func main() {}
