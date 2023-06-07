package main

import (
	"fmt"
	"math"
)

func main() {
	var points [][]int
	points = [][]int{{1, 1}, {1, 3}, {3, 1}, {3, 3}, {4, 1}, {4, 3}}
	points = [][]int{{1, 1}, {1, 3}, {3, 1}, {3, 3}, {2, 2}}
	points = [][]int{{3, 2}, {0, 0}, {3, 3}, {3, 4}, {4, 4}, {2, 1}, {4, 3}, {1, 0}, {4, 1}, {0, 2}}
	fmt.Println(minAreaRect(points))
}

type Points [][]int

func makeSortPoints(points [][]int) Points {
	p = Points{}
	p = append(p, points...)
	return Points{}
}

func minAreaRect(points [][]int) int {
	minArea := math.MaxInt64
	for i, point := range points {
		minArea = findMinArea(points[i+1:], point, minArea)
	}
	if minArea == math.MaxInt64 {
		minArea = 0
	}
	return minArea
}

func contains(list []int, num int) bool {
	for _, item := range list {
		if num == item {
			return true
		}
	}
	return false
}

func findMinArea(points [][]int, point []int, minArea int) int {
	topLeftCorner := []int{}
	bottomRightCorner := []int{}
	for _, p := range points {
		if p[0] == point[0] {
			topLeftCorner = append(topLeftCorner, p[1])
		} else if p[1] == point[1] {
			bottomRightCorner = append(bottomRightCorner, p[0])
		} else if contains(bottomRightCorner, p[0]) && contains(topLeftCorner, p[1]) {
			width := math.Abs(float64(point[0] - p[0]))
			height := math.Abs(float64(point[1] - p[1]))
			area := int(width * height)
			if area < minArea {
				minArea = area
			}
		}
	}
	return minArea
}
