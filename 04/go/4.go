package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Range(start int, end int) []int {
	r := make([]int, 0)
	for i := start; i <= end; i++ {
		r = append(r, i)
	}
	return r
}

func main() {
	file, err := os.Open("4/input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	total_4_1 := 0
	total_4_2 := 0

	for scanner.Scan() {
		pair := strings.Split(scanner.Text(), ",")
		p1 := strings.Split(pair[0], "-")
		p2 := strings.Split(pair[1], "-")
		p1_start, _ := strconv.Atoi(p1[0])
		p1_end, _ := strconv.Atoi(p1[1])
		p2_start, _ := strconv.Atoi(p2[0])
		p2_end, _ := strconv.Atoi(p2[1])
		p1_range := Range(p1_start, p1_end)
		p2_range := Range(p2_start, p2_end)

		if p1_start >= p2_start && p1_end <= p2_end || p2_start >= p1_start && p2_end <= p1_end {
			total_4_1 += 1
		}

		issubset := 0
		for _, i := range p1_range {
			for _, j := range p2_range {
				if i == j {
					issubset = 1
				}
			}
		}
		total_4_2 += issubset

	}
	fmt.Println("4.1:", total_4_1)
	fmt.Println("4.2:", total_4_2)
}
