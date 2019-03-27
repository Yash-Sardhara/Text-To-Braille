function printBraille() {
    var x = document.getElementById('myTextArea').value;
    console.log(x);
    var chars = []
    for (var i=0; i<x.length; i++) {
        chars.push(x[i]);
    }
    console.log(chars);
    // $.ajax({
    //     type:"POST",
    //     contentType: "application/json;charset=utf-8",
    //     url:"/printBr",
    //     traditional: "true",
    //     data: JSON.stringify({chars}),
    //     dataType: "json"
    // })
}

