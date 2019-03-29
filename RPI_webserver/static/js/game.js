var validAlphabets = new Set(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T", 
    "U","V","W","X","Y","Z"]); 
var validNums = new Set(["0","1","2","3","4","5","6","7","8","9"]);
var validPuncs = new Set(["#",";","'","?","!",":","-",","," ", "."])

var total = validAlphabets.length + validNums.length + validPuncs.length;
console.log(total);
function printBraille() {
    var count = 0;
    Math.floor((Math.random() * total) + 1);
    
    // send request to server
    // $.ajax({
    //     type:"POST",
    //     contentType: "application/json;charset=utf-8",
    //     url:"/getText",
    //     traditional: "true",
    //     data: JSON.stringify({input}),
    //     dataType: "json"
    // })

    console.log(sum);
    return sum;
}




