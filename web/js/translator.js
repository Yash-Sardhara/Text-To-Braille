var validChars = new Set(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T", 
    "U","V","W","X","Y","Z","#","0","1","2","3","4","5","6","7","8","9",";","'","?","!",":","-",","," "]); 

function printBraille() {
    var invalidInput = false;
    var input = document.getElementById('myTextArea').value;
    console.log(input);
    for (var i=0; i<input.length; i++) {
        if(!validChars.has(input[i])){
            var myText = document.getElementById('remind');
            myText.innerHTML = "Invalid Input: ".concat(input[i],'.');
            return;
        }
    }

    var myText = document.getElementById('remind');
    myText.innerHTML = "(Printing in progress... You can resubmit after the robot finishes printing)";
    $('button').prop('disabled', true);
    $.ajax({
        type:"POST",
        contentType: "application/json;charset=utf-8",
        url:"/getText",
        traditional: "true",
        data: JSON.stringify({input}),
        dataType: "json"
    })
    return x;
    
    
}


