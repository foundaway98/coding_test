function solution(arr) {
    let val = 0
    for (item of arr){
        val += item
    }
    return val / arr.length
}