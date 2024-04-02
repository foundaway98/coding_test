function solution(id_pw, db) {
    var answer = '';
    for(let item of db){
        if(id_pw[0] === item[0]){
            if(id_pw[1] === item[1]){
                return "login"
            } else if(id_pw[1] !== item[1]){
                return "wrong pw"
            }
        }
    }
    return "fail";
}