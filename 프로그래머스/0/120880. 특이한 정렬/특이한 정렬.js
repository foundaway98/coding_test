function solution(numlist, n) {
    numlist.sort((a,b) => {
        if(Math.abs(n - a) > Math.abs(n-b)){
            return 1
        } else if(Math.abs(n-a) < Math.abs(n-b)){
            return -1
        } else if(Math.abs(n-a) === Math.abs(n-b)){
            if(a > b){
                return -1
            } else if(a === b){
                return 0
            } else{
                return 1
            }
        }
    })
    
    return numlist;
}