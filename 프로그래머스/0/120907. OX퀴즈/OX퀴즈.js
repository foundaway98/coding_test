function solution(quiz) {
    var answer = [];
    for(let q of quiz){
        let qq = q.split(" ")
        let correct = 0
        if(qq[1] === "-"){
            correct = parseInt(qq[0]) - parseInt(qq[2])
        } else {
            correct = parseInt(qq[0]) + parseInt(qq[2])
        }
        if(correct == qq[4]){
            answer.push("O")
        } else {
            answer.push("X")
        }
    }
    return answer;
}