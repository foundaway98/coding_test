function solution(k, m, score) {
    var answer = 0;
    score.sort()
    boxCnt = parseInt(score.length / m)
    for(let i = 0; i< boxCnt; i++){
        box = []
        for(let j = 0; j<m; j++){
            box.push(score.pop())           
        }
        box.sort()
        answer += (box[0] * m)
    }
    return answer;
}