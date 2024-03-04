function solution(number, limit, power) {
    var answer = 0;
    let knights = [1]
    
    for(let knight=2;knight<=number;knight++){
        cnt = 0
        for(let i = 1; i<=parseInt(Math.sqrt(knight));i++){
            if(knight % i == 0){
                cnt += 1
            }
        }
        cnt *= 2
        if(Math.sqrt(knight) - parseInt(Math.sqrt(knight)) === 0){
            cnt -= 1
        }
        if(cnt > limit){
            cnt = power
        }
        knights.push(cnt)
    }
    
    for(let p of knights){
        answer += p
    }
    
    return answer;
}