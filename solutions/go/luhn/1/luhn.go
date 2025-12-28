package luhn

import "unicode"

func Valid(id string) bool {
    new_id := []rune{}
    for _, digit := range id {
        if unicode.IsDigit(digit) {
            new_id = append(new_id, digit)
        } else if string(digit) != " " {
            return false
        }
    }
    len_new_id := len(new_id)
	if len_new_id < 2 {
        return false
    }
    len_mod_2 := len_new_id % 2
    val_acc := 0
    for idx, digit := range new_id {
        digit_int := int(digit) - int('0')
        if idx % 2 == len_mod_2 {
            if digit_int > 4 {
                val_acc += 2 * digit_int - 9
            } else {
                val_acc += 2 * digit_int
            }
        } else {
			val_acc += digit_int
        }
    }
    return val_acc % 10 == 0
}
