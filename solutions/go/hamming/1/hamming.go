package hamming

import "fmt"

func Distance(a, b string) (int, error) {
    if len(a) != len(b) {
        return 0, fmt.Errorf("unequal string list; got lengths %d and %d", len(a), len(b))
    }
	dist_acc := 0
    for idx, _ := range a {
        if a[idx] != b[idx] {
            dist_acc += 1
        }
    }
    return dist_acc, nil
}
