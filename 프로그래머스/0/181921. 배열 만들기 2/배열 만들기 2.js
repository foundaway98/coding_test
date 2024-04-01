function solution(l, r) {
    let answer = []
    for(let i = l; i<=r; i++){
        let tmp = i.toString().split("")
        if(tmp.every(num => num == 0 || num == 5)){
            answer.push(parseInt(tmp.join("")))
        }
    }
    if(answer.length === 0){
        answer.push(-1)
    }
    return answer
}