var validChars = new Set(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T", 
    "U","V","W","X","Y","Z","#","0","1","2","3","4","5","6","7","8","9",";","'","?","!",":","-",","," "]); 

function printBraille() {
    var input = document.getElementById('myTextArea').value;
    console.log(input);
    // check if the input is valid
    if (input.length == 0) {
        document.getElementById('modalTitle').innerHTML = "Submission Failed!";
        document.getElementById('modalBody').innerHTML = "Empty input";
        return;
    }
    for (var i=0; i<input.length; i++) {
        if(!validChars.has(input[i])){
            document.getElementById('modalTitle').innerHTML = "Submission Failed!";
            document.getElementById('modalBody').innerHTML = "Invalid Input: ' ".concat(input[i], " '", '.');
            return;
        }
    }
    // disable button and display note to user
    document.getElementById('modalTitle').innerHTML = "Submission Successful!";
    document.getElementById('modalBody').innerHTML = "Printing in progress...";
    document.getElementById('remind').innerHTML = "(Printing in progress... You can resubmit after the robot finishes printing)";
    $('button').prop('disabled', true);
    // send request to server
    $.ajax({
        type:"POST",
        contentType: "application/json;charset=utf-8",
        url:"/getText",
        traditional: "true",
        data: JSON.stringify({input}),
        dataType: "json"
    })

}

window.onload = loadText()

function loadText() {
    $.ajax({
        type:"GET",
        url:"/updateText",
        dataType:"json",
        async:false,
        success: function(data){
            text = data
            updateText(text)
        },
        complete: function(){
            setTimeout(loadText, 1000);
        }
    })

};

function updateText(text) {
    console.log(text)
    document.getElementById('textFromKeypad').innerHTML = text;
}

