/*
solution..!
- 자바스크립트 난독화 해제를 먼저 해야함
    - https://beautifier.io/
- 최초 생성하는 secureGame을 보면 BincScore로 점수를 올리고 getScore로 현재 점수를 가져오고 있음
- 따라서 별도 변수를 만들고 생성자 선언을 한다음 반복문으로 점수를 올리고 마지막에 high-score 호출
*/


const injection = () => {
    const injection = new secureGame();
    for(let i=0; i<1000000; i++){
        injection['BincScore']();
    }

    // 점수 확인
    injection['getScore']();


    // high-scores 호출
    // fetch api를 써도 되는데 그냥 원본소스 그대로 사용
    updateToken();
    $['ajax']({
        type: 'POST',
        url: 'high-scores.php',
        data: 'token=' + token + '&score=' + test['getScore'](),
        success: function(_0x8618x19) {
            showHighScores(_0x8618x19)
        }
    })
}