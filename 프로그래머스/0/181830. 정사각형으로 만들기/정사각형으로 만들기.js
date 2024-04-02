function solution(arr) {
    let answer = []
    if(arr.length === arr[0].length){
        return arr
    } else {
        if(arr.length > arr[0].length){
            for(let item of arr){
                let tmp = [...item]
                for(let i = 0;i<arr.length - arr[0].length;i++){
                    tmp.push(0)
                }
                answer.push(tmp)
            }
        } else {
            let d = arr[0].length - arr.length
            for(let i=0;i<d;i++){
                arr.push(new Array(arr[0].length).fill(0))
            }
            answer = arr
        }
    }
    
    return answer;
}