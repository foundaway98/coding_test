function solution(score) {
    let answer = []
    let s = score.map((m) => (m[0] + m[1]) / 2)
    let sortedS = [...s].sort((a,b) => a-b).reverse()
    let scoreBoard = {}
    let grade = 0
    for(let item of sortedS){
        grade++
        if(scoreBoard[item]){
            continue
        }
        scoreBoard[item] = grade
    }
    for(let score of s){
        answer.push(scoreBoard[score])
    }
    return answer;
}