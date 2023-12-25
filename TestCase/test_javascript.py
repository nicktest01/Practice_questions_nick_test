# -*- coding:utf-8 -*-
"""
從程式中(JS),找出錯誤,並提出改善方案
function FindCommonElements(arr1,arr2){
    var CommonElements = [];

    for (let i=0;i<=arr1.length;i++){
        for(let j = 0 i<=arr2.length;j++){
            if(arr1[i] === arr2[j]){
                CommonElements.append(arr1[i]);
            }
        }
    }
    return  CommonElements;
}
Console.log (FindCommonElements([1,2,3,4],[3,4,5,6]))
期望輸出:[3,4]
"""

function FindCommonElements(arr1, arr2) {
    var CommonElements = [];

    for (let i = 0; i < arr1.length; i++) {
        #修正迴圈條件錯誤：j = 0; j < arr2.length
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) {
                #append用法錯誤：append → push
                CommonElements.push(arr1[i]);
            }
        }
    }
    return CommonElements;
}

Console.log(FindCommonElements([1, 2, 3, 4], [3, 4, 5, 6]));
#期望輸出:[3, 4]