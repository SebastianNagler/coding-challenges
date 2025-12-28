package diffsquares

func SquareOfSum(n int) int {
	sum := int(n * (n + 1) / 2)
    return sum * sum
}

func SumOfSquares(n int) int {
	return int(((n * n * n) + int(n * (n + 1) / 2) + (n * n)) / 3)
}

func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
