package main

import (
	"fmt"
)

func main() {
	var input string
	fmt.Print("Введите текст: ")
	fmt.Scanln(&input)

	// Хэширование методом деления
	hashDivision := hashDivision(input)
	fmt.Printf("Хэш методом деления: %d\n", hashDivision)

	// Хэширование методом CRC-32
	hashCRC32 := crc32(input)
	fmt.Printf("Хэш CRC-32: %08X\n", hashCRC32)
}

// Хэширование методом деления
func hashDivision(text string) uint32 {
	var hash uint32
	for _, char := range text {
		hash = (hash*31 + uint32(char)) % 1000000007
	}
	return hash
}
func crc32(text string) uint32 {
	const polynomial uint32 = 0xEDB88320
	var table [256]uint32

	// Инициализация таблицы
	for i := 0; i < 256; i++ {
		crc := uint32(i)
		for j := 0; j < 8; j++ {
			if crc&1 != 0 {
				crc = (crc >> 1) ^ polynomial
			} else {
				crc >>= 1
			}
		}
		table[i] = crc
	}

	// Вычисление CRC-32
	var crc uint32 = 0xFFFFFFFF
	for _, char := range text {
		crc = (crc >> 8) ^ table[(crc^uint32(char))&0xFF]
	}
	return ^crc
}
