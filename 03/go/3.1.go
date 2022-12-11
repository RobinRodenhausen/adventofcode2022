package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"unicode"
)

func main() {
	file, err := os.Open("3/input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		line := scanner.Text()
		first := line[:len(line)/2]
		second := line[len(line)/2:]

		duplicate := ' '

		for _, f := range first {
			for _, s := range second {
				if f == s {
					duplicate = f
				}
			}
		}
		if unicode.IsUpper(duplicate) {
			total += int(duplicate) - 38
		} else {
			total += int(duplicate) - 96
		}
	}
	fmt.Println("3.1:", total)
}
