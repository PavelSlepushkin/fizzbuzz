#A Rule of Divisibility by 7 - codewars.com
#!/bin/bash
seven () {
    # your code
    i='0'
    res=${1}
    while ((${#res} >2)) ; do
        last_digit=${res: -1}
        start_digits=${res: 0: -1}
        #res=$((start_digits - 2 * last_digit))
        res=$(echo "${start_digits}-2*${last_digit}"|bc)
        i=$((i + 1))
    done
    echo "$res, $i"        
}
seven "$1"