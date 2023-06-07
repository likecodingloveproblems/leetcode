package main

import (
	"encoding/json"
	"fmt"
	"reflect"
)

type Bird struct {
	Species     string
	Description string
	Age         int
}

func main() {
	birdJson := `{"species": "pigeon","description": "likes to perch on rocks", "age": 26}`
	var bird Bird
	json.Unmarshal([]byte(birdJson), &bird)

	birdByte, _ := json.Marshal(bird)
	newBird := fmt.Sprintf("{%s: %s}", reflect.TypeOf(bird).Name(), string(birdByte))
	fmt.Println(newBird)

}
