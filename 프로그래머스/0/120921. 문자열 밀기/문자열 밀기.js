function solution(A, B) {
    let answer = 0
    if(A === B){
        return 0
    }
    a = A.split("").reverse()
    b = B.split("").reverse()
    for(let i = 1;i<=a.length;i++){
        a.push(a.shift())
        if(a.join("") == b.join("")){
            answer += i
            break
        }
    }
    if(answer === 0){
        return -1
    } else{
        return answer
    }
}