package strand

import "strings"

var comp_map = map[string]string{"G": "C", "C": "G", "T": "A", "A": "U"}

func ToRNA(dna string) string {
    var builder strings.Builder
    for _, nuc := range dna {
        builder.WriteString(comp_map[string(nuc)])
    }

    return builder.String()
}
