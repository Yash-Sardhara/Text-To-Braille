var validChars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","#",";","'","?","!",":","-",","," ","."];
var validCharsSize = 46;
var attempts = 3;

var validNums = new Set(["0","1","2","3","4","5","6","7","8","9"]);


var randomString = "";
var rChar = "a";

function sendPrint() {
    var input = document.getElementById('mySelect').value;
    console.log(input);

    var isNum = false;
    if (input == 0) {
        // disable button and display note to user
        document.getElementById('mTitle').innerHTML = "Submit something!";
        document.getElementById('mBody').innerHTML = "Choose a number for the robot to print.";
        document.getElementById('message').innerHTML = "";
        $("#exampleModal").modal();
        return;
    }

    // disable button and display note to user
    document.getElementById('mTitle').innerHTML = "Submission Successful!";
    document.getElementById('mBody').innerHTML = "Printing in progress...";
    document.getElementById('message').innerHTML = "You have 3 attempts. You have to win (or refresh) to replay.";
    $("#exampleModal").modal();
    $('#submitGame').prop('disabled', true);

    for (var i=0; i < input; i++) {
        rChar = validChars[Math.floor(Math.random() * validCharsSize)];
        console.log(rChar);
        randomString = randomString.concat(rChar);

        // maybe check how many braille characters that is
    }
    console.log(randomString);

    // send request to server
    // $.ajax({
    //     type:"POST",
    //     contentType: "application/json;charset=utf-8",
    //     url:"/getText",
    //     traditional: "true",
    //     data: JSON.stringify({input}),
    //     dataType: "json"
    // })

}

function verifyAnswer() {
    var input = document.getElementById('gameAnswer').value;
    console.log(input);
    if (randomString == "") {
        document.getElementById('mTitle').innerHTML = "Submit something!";
        document.getElementById('mBody').innerHTML = "Choose a number for the robot to print.";
        $("#exampleModal").modal();
        document.getElementById('message').innerHTML = "";
        return;
    }
    if (attempts > 0) {
        if (input == randomString) {
            document.getElementById('mTitle').innerHTML = "Answer Correct!";
            document.getElementById('mBody').innerHTML = "You won!!!!";
            $("#exampleModal").modal();
            document.getElementById('message').innerHTML = "Do you want to replay?";
            $('#submitGame').prop('disabled', false);
            randomString = "";
            attempts = 3;
            console.log("win");
        } else {
            attempts--;
            if (attempts == 0) {
                attempts--;
                document.getElementById('mTitle').innerHTML = "Answer Incorrect...";
                document.getElementById('mBody').innerHTML = "You lost!";
                $("#exampleModal").modal();
                document.getElementById('message').innerHTML = "You have no more attempts. Refresh to replay.";
                $('#checkAnswer').prop('disabled', true);
                console.log("lose");
            } else {
                document.getElementById('mTitle').innerHTML = "Answer Incorrect...";
                document.getElementById('mBody').innerHTML = "Try again!";
                $("#exampleModal").modal();
                document.getElementById('message').innerHTML = "You have ".concat(attempts,  " attempts left. You have to win (or refresh) to replay.");
                console.log("trying");
            }
        }  
    }
}

$("cheatSheet").hover(function(){
    $(this).css("background-color", "yellow");
    }, function(){
    $(this).css("opacity", "0");
  });

