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
		lines := make([]string, 0)
		lines = append(lines, scanner.Text())
		for i := 0; i < 2; i++ {
			scanner.Scan()
			lines = append(lines, scanner.Text())
		}

		duplicate := ' '

		for _, f := range lines[0] {
			for _, s := range lines[1] {
				for _, t := range lines[2] {
					if f == s && f == t {
						duplicate = f
					}
				}
			}
		}
		if unicode.IsUpper(duplicate) {
			total += int(duplicate) - 38
		} else {
			total += int(duplicate) - 96
		}
	}
	fmt.Println("3.2:", total)
}
