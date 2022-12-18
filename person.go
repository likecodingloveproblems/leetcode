package main

type IPerson interface {
}

type person struct {
	name   string
	age    int
	gender rune
}

func NewPerson() *person {
	return &person{"ali", 30, 'M'}
}
