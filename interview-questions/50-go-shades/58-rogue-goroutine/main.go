package main

import (  
	"fmt"
	"runtime"
)

func main() {  
	done := false

	go func(){
			done = true
	}()

	for !done {
			runtime.Gosched()
	}
	fmt.Println("done!")
}