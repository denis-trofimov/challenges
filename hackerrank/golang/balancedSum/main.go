package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'balancedSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func balancedSum(arr []int32) int32 {
    // Write your code here
    lSum := make([]int32, len(arr))
    rSum := make([]int32, len(arr))
  
    // p := int(len(arr) / 2) 
    var sum, rSum2 int32
    
    for i, v := range arr {
        backindex := len(arr) - 1 - i
        sum += v
        lSum[i] = sum
        rSum2 += arr[backindex]
        rSum[backindex] = rSum2
    }

    counter := 0
    step := len(arr) / 2
    p := step
    for {
        step /= 2
        if step == 0 {
            step = 1
        }
        if lSum[p-1] == rSum[p+1]{
            return int32(p)
        } else {
            if lSum[p-1] < rSum[p+1] {
                // go right
                p += step
            } else {
                // go left
                p -= step
            }
        }
        
        counter++
        if counter > 1000001 {
            return -1
        }
    }
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    arrCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)

    var arr []int32

    for i := 0; i < int(arrCount); i++ {
        arrItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    result := balancedSum(arr)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
