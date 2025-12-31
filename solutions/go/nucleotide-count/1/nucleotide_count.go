package dna

import "fmt"

type DNA string

type Histogram map[rune]int

func (d DNA) Counts() (Histogram, error) {
	var h Histogram
    h = Histogram{rune('A'): 0, rune('C'): 0, rune('G'): 0, rune('T'): 0}
    for _, nuc := range d {
        nuc_num, exists := h[nuc]
        if !exists {
            return h, fmt.Errorf("%s is not a nucleotide initial", string(nuc))
        } else {
            h[nuc] = nuc_num + 1
        }
    }
	return h, nil
}
