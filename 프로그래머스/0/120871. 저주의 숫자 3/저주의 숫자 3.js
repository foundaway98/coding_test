function solution(n) {
    let cnt = 1
    let num = 1
    while(num < n){
        cnt++
        num++
        while(cnt%3 === 0 || cnt.toString().indexOf("3") !== -1){
            cnt++
        }
    }
    return cnt
    
}