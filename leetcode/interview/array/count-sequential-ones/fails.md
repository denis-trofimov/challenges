# Fails

## WA wrong answer

```go
package main

import (
	"fmt"
)

func main() {
	var n int
	result := 0
	l := 0

	for {
		r, err := fmt.Scanf("%d\n", &n)
		if err != nil || r == 0 {
			break
		}

		if n == 1 {
			l++
		} else {
			result = max(result, l)
			l = 0
		}
	}

	fmt.Println(result)
}
```
