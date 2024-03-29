function solution(num, total) {
    var answer = [];
    let start = 0
    let mid = (num-1) % 2 == 1 ? Math.floor(num/2) : -1
    if(mid === -1){
        start = (total - num * ((num - 1)/2)) / num
    } else {
        start = (total - (num * (Math.floor((num-1)/2)) + mid)) / num
    }
    
    for(let c=0;c<num;c++){
        answer.push(start++)
    }
    
    return answer;
}