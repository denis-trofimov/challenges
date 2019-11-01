package main

func reverse(x int) int {
    b := []int{}
    negative := false
    if x < 0 {
        negative = true
        x = -x
    }
    for x >= 10 {
        b = append(b, x % 10)
        x /= 10
    }
    b = append(b, x)
    x = 0
    for _, d := range b {
        x = x * 10 + d
    }
    if x > 2147483648 {
        return 0
    }
    if negative {
        return -x
    }
    return x
}


func main() {
	x := 10
	x = reverse(x)
}
