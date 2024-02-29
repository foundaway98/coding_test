function solution(k, score) {
    var answer = [];
    const table = [];

    for(i=0;i<score.length;i++){
        let point = score[i]
        if (table.length < k){
            table.push(point)
        }
        else{
            if(point > table[table.length - 1]){
                table.pop()
                table.push(point)
            }
        }
        table.sort((a,b) => {
            if(a > b) return 1
            else return -1
        })
        table.reverse()
        answer.push(table[table.length-1])
        
    }
    return answer;
}