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
		result := (int(input[1][0]) - 88) * 3

		total += result

		switch result {
		case 0:
			if enemy == 1 {
				total += 3
			} else {
				total += enemy - 1
			}

		case 3:
			total += enemy
		case 6:
			total += (enemy % 3) + 1
		}

	}
	fmt.Println("2.2:", total)
}
