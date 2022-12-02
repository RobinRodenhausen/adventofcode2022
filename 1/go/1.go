package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func sum(slice []int) int {
	result := 0
	for _, value := range slice {
		result += value
	}
	return result
}

func main() {
	file, err := os.Open("1/input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	total := 0
	calories := make([]int, 0)

	for scanner.Scan() {
		if scanner.Text() == "" {
			calories = append(calories, total)
			total = 0
		} else {
			value, _ := strconv.Atoi(scanner.Text())
			total += value
		}
	}
	sort.Ints(calories)
	fmt.Println("1.1:", calories[len(calories)-1])
	fmt.Println("1.2:", sum(calories[len(calories)-3:]))
}
