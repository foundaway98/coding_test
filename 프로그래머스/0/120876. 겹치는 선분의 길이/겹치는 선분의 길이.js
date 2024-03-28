function solution(lines) {
    let answer = 0
    let arr = new Array(200).fill(0)
    for(let items of lines){
        for(let s = items[0] + 100; s<items[1]+100; s++){
            arr[s] += 1
        }
    }
    for(let item of arr){
        if(item > 1){
            answer+=1
        }
    }
    
    return answer;
}