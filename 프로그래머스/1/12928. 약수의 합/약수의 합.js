function solution(n) {
    let sumArr = []
    let result = 0
    for(let i = 1; i<=n; i++){
        if(n % i == 0){
            sumArr.push(i)
        }
    }
    for(item of sumArr){
        result += item
    }
    return result
}