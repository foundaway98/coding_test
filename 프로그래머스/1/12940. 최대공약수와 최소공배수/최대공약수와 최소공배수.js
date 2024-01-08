//최대공약수
//유클리드 호제법
function minMax(n,m){
    let max, min = 0
    if(n > m){
        max = n
        min = m
    }
    else{
        max = m
        min = n
    }
    return [max, min]
}


function solution(n, m) {
    let result = []
    let arr= minMax(n,m)
    let max = arr[0]
    let min = arr[1]
    
    while(max % min != 0){
        let tmp = minMax(min, max%min)
        max = tmp[0]
        min = tmp[1]
    }
    result.push(min)
    result.push(n*m/min)
    return result
    
}