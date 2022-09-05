function controlCar(scanArray){        
    // -1 : left, 0 : straight, 1: right
    const maxLimit = 13;
    const defaultLimit = 12;    
    const frontL = scanArray[7];
    const frontR = scanArray[9];
    const frontC = scanArray[8];
    const basicIndex = [7,8,9];
    let result = 0;
    
    console.log("============== flag start ==============");
    if(frontL >= maxLimit && frontR >= maxLimit && frontC >= maxLimit){ // 직진
        console.log("keep staright...");
        result = 0;
        
    }else{  // 핸들을 틀거임        
        console.log("need avoid..!!!!", frontL, frontR, frontC);

        let rightRoad = scanArray[basicIndex[2]+=2] * 1;
        let rightRoadClose = scanArray[basicIndex[2]+=1] * 1;
        let rightSide = scanArray[basicIndex[2]] * 1;
        let leftRoad = scanArray[basicIndex[0]-=2] * 1;
        let leftRoadClose = scanArray[basicIndex[0]-=1] * 1;
        let leftSide = scanArray[basicIndex[0]] * 1;

        if(frontL < defaultLimit ) console.log("need to go right", rightRoad, rightRoadClose);
        if(frontR < defaultLimit ) console.log("need to go left", leftRoad, leftRoadClose);
        if(frontC < defaultLimit ) console.log("front check : ", rightRoad, rightRoadClose, leftRoad, leftRoadClose);

        console.log(`left flag : ${(leftRoad > 8 && frontR < 8)}, right flag : ${(rightRoad > 8 && frontL < 8)}`);
        
        // left
        if(frontR < defaultLimit){
            if(leftRoad > defaultLimit){
                console.log("go to left more")
                result = -5;            
            }

            if(leftRoadClose > defaultLimit){
                console.log("go to left")
                result = -1;            
            }


            if(rightSide < defaultLimit) {
                console.log("rightSide check than go left")
                result = -1;
            }

            
            if(rightRoad === 0 && rightRoadClose === 0){
                console.log("go to left2")
                result = -1;
            }
        }

        // right
        if(frontL < defaultLimit){
            if(rightRoad > defaultLimit){
                console.log("go to right more")
                result = 5;            
            }

            if(rightRoadClose > defaultLimit){
                console.log("go to right ")
                result = 1;            
            }

            if(leftSide < defaultLimit) {
                console.log("leftside check than go right")
                result = 1;
            }

            if(leftRoad === 0 && leftRoadClose === 0) {
                console.log("go to right2")
                result = 1;                
            }
        }     
        
        // center check
        if(frontC < defaultLimit){
            
            if(leftRoad > defaultLimit){
                console.log("(straight) go to left more")
                result = -5;            
            }

            if(leftRoadClose > defaultLimit){
                console.log("(straight) go to left")
                result = -1;            
            }

            
            if(rightRoad > defaultLimit){
                console.log("(straight) go to right more")
                result = 5;            
            }

            if(rightRoadClose > defaultLimit){
                console.log("(straight) go to right")
                result = 1;            
            }

            
            if(rightRoad === 0 && rightRoadClose === 0) {
                console.log("(straight) go to left")
                result = -1;
            }

            
            if(leftRoad === 0 && leftRoadClose === 0){
                console.log("(straight) go to right2")
                result = 1;
            }
        }
                        
    }
    console.log(`result : ${result}`)
    console.log("============== flag end ==============");
    return result;
    


/*
    console.log("front : " , scanArray[8])
    console.log("right side : " , scanArray[9])
    console.log("left side : " , scanArray[7])
    if(scanArray[8] >= 8 && scanArray[8] <= 10){ // 전방에 장애물이 있는 경우
        // 왼쪽과 오른쪽 중 갈 수 있는 곳을 판단
        // 왼쪽 체크 5, 오른쪽 체크 11
        if(scanArray[5] > scanArray[11]) {      // 1 단위당 한칸씩 옮겨가는듯??
            console.log("turn left");
            return -5;
        }else{
            console.log("turn right");
            return 5;
        }
        
    }else if(scanArray[9] <= 4 || scanArray[10] <= 4){ // 오른쪽 사이드에 장애물이 있는 경우
        console.log("turn right");
        return -5;
    }else if(scanArray[7] <= 4 || scanArray[6] <= 4){ // 왼쪽 사이드에 장애물이 있는 경우
        console.log("turn left");
        return 5
    }else{
        return 0;
    }
*/
    /* 자 체크해야할거
    시버ㅗㄹ다시해
        - 전방체크
        7,8,9 같이 확인 -> 세개 다 9 이하인 경우에는 계속 직진할거임 이중 하나라도 안맞으면 핸들을 틀어야함...!!!
        
        - 
    */
}

