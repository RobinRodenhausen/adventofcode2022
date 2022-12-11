package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("2/input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		input := strings.Split(scanner.Text(), " ")

		enemy := int(input[0][0]) - 64
		me := int(input[1][0]) - 87

		total += me

		if enemy == me {
			total += 3
		} else if me > enemy%3 && me-enemy%3 == 1 {
			total += 6
		}

	}
	fmt.Println("2.1:", total)
}
