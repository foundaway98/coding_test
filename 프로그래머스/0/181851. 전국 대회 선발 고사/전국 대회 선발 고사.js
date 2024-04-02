function solution(rank, attendance) {
    var answer = [];
    let scoreBoard = {}
    for(let i=1; i<=rank.length; i++){
        scoreBoard[i] = rank.indexOf(i)
    }
    
    for(let i=1;i<=rank.length;i++){
        if(attendance[scoreBoard[i]]){
            answer.push(scoreBoard[i])
        }
        if(answer.length === 3){
            break
        }
    }
    
    return answer[0] * 10000 + answer[1] * 100 + answer[2];
}