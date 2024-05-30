/*
 * https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
 * Terminated due to timeout :(
 * Complete the 'arrayManipulation' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

 package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

// func arrayManipulation(n int32, queries [][]int32) int64 {
// 	points := make([]int32, n+1)
// 	for _, query := range queries{
// 			points[query[0]-1] += query[2]
// 			points[query[1]] -= query[2]
// 	}

// 	var maximum, level int64
// 	for pos, val := range points {
// 			fmt.Println(pos, val)
// 			level += int64(val)
// 			if level > maximum {
// 					maximum = level
// 			}
// 	}

// 	return maximum
// }

func arrayManipulation(n int32, queries [][]int32) int64 {
	borders := make([]border, 0)
	for _, query := range queries{
			borders = insert_binary_search(borders, border{query[0], int64(query[2])})
			borders = insert_binary_search(borders, border{query[1]+1, int64(-query[2])})
	}

	var maximum, level int64
	for _, item := range borders{
			fmt.Println(item.position, item.value)
			level += item.value
			if level > maximum {
					maximum = level
			}
	}

	return maximum
}

type border struct {
	position int32
	value int64
}

func insert(bl []border, b border) []border {
	for i, item := range bl{
			switch {
					case item.position == b.position:
							bl[i] = border{b.position, item.value + b.value}
							return bl
					case item.position > b.position:    
							bl = append(bl[:i+1], bl[i:]...)
							bl[i] = b    
							return bl
			}
	}
	
	return append(bl, b)
}

func insert_binary_search(points []border, b border) []border {
	if len(points) == 0 {
			return append(points, b)
	}
	
	i := len(points)/2
	for span := len(points)/4; span > 0; span /=2 {
			switch {
					case points[i].position == b.position:
							points[i].value += b.value
							return points
					case points[i].position > b.position:    
							i -= span
					default:
							i += span
			}
	}

	points = append(points[:i+1], points[i:]...)
	if points[i].position < b.position {       
			points[i+1] = b    
			return points
	}
	
	points[i] = b    
	return points
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	n := int32(nTemp)

	mTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	m := int32(mTemp)

	var queries [][]int32
	for i := 0; i < int(m); i++ {
			queriesRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")

			var queriesRow []int32
			for _, queriesRowItem := range queriesRowTemp {
					queriesItemTemp, err := strconv.ParseInt(queriesRowItem, 10, 64)
					checkError(err)
					queriesItem := int32(queriesItemTemp)
					queriesRow = append(queriesRow, queriesItem)
			}

			if len(queriesRow) != 3 {
					panic("Bad input")
			}

			queries = append(queries, queriesRow)
	}

	result := arrayManipulation(n, queries)

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
