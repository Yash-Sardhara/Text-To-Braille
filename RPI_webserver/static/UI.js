// make the joystick movable
document.getElementById('joystick').onmousedown = drag;
document.getElementById('joystick').onmousemove = move;
document.getElementById('joystick').onmouseup = drop;

var obj, x, y, prev_x, prev_y, cur_x, cur_y, theta, r;
var x_center = 850;
var y_center = 300;
var motorspeed = [0, 1];
var baseSpeed = [0];
var states = [0];

function drag(e) {
    obj = e.target;
    prev_x = x - obj.offsetLeft;
    prev_y = y - obj.offsetTop;
}

function move(e) {
    if (e.pageX) {
        x = e.pageX;
        y = e.pageY;
    }

    if (obj) {
        cur_x = x - prev_x;
        cur_y = y - prev_y;
        r = Math.sqrt((cur_x - x_center) * (cur_x - x_center) + (cur_y - y_center) * (cur_y - y_center));
        if (r <= 200) {
            obj.style.left = (cur_x) + 'px';
            obj.style.top = (cur_y) + 'px';

            theta = Math.atan(-(cur_y - y_center) / (cur_x - x_center));
            if ((cur_x - x_center) < 0 && -(cur_y - y_center)< 0) {
                theta = - Math.PI + theta;
            } else if ((cur_x - x_center) < 0 && -(cur_y - y_center)> 0){
                theta = Math.PI + theta;
            }
            console.log("theta: %f, r: %f", theta, r);
            motorspeed[0] = leftMotor(theta, r);
            motorspeed[1] = rightMotor(theta, r);
            console.log(motorspeed);
            $.ajax({
                type:"POST",
                contentType: "application/json;charset=utf-8",
                url:"/moveJoystick",
                traditional: "true",
                data: JSON.stringify({motorspeed}),
                dataType: "json"
            })
        }
        
    }
}

function rightMotor(t, r) {
    if (t >= 0){
        return (t / Math.PI) *  r / 200 * 0.6 + 0.4;
    } else {
        return (t / Math.PI) *  r / 200 * 0.6 - 0.4;
    }
}

function leftMotor(t, r) {
    if (t >= 0) {
        return (Math.PI - t ) / Math.PI * r / 200 * 0.6 + 0.4;
    } else {
        return (-Math.PI - t)/ Math.PI * r / 200 * 0.6 - 0.4;
    }
}

function drop() {
    obj.style.left = (x_center) + 'px';
    obj.style.top = (y_center) + 'px';
    obj = false;
    $.get('/stop');
}

document.getElementById('forward').onmousedown = moveForward;
document.getElementById('backward').onmousedown = moveBackward;
document.getElementById('left').onmousedown = moveLeft;
document.getElementById('right').onmousedown = moveRight;

document.getElementById('forward').onmouseup = stop;
document.getElementById('backward').onmouseup = stop;
document.getElementById('left').onmouseup = stop;
document.getElementById('right').onmouseup = stop;


function moveForward() {
    console.log("go straight");
    $.get('/forward');
}

function moveBackward() {
    console.log("go back");
    $.get('/backward');
}

function moveLeft() {
    console.log("turn left");
    $.get('/turnLeft');
}

function moveRight() {
    console.log("turn right");
    $.get('/turnRight');
}

function stop() {
    console.log("stop");
    $.get('/stop');
}


function changeState() {
    var state = document.getElementById('toggleSwitch');
    if (state.textContent == "line-following") {
        state.textContent = "remote-controlling";
        states[0] = 1
        console.log(state.textContent);
    } else {
        state.textContent = "line-following";
        states[0] = 0
        console.log(state.textContent);
    }
    $.ajax({
        type:"POST",
        contentType: "application/json;charset=utf-8",
        url:"/changeState",
        traditional: "true",
        data: JSON.stringify({states}),
        dataType: "json"
    })
}

document.getElementById('speedRange').onmousemove = changeSpeed;

function changeSpeed() {
    var speed = document.getElementById('speedRange').value / 100 * 0.6 + 0.4;
    console.log(speed);
    baseSpeed[0] = speed;
    $.ajax({
        type:"POST",
        contentType: "application/json;charset=utf-8",
        url:"/changeBaseSpeed",
        traditional: "true",
        data: JSON.stringify({baseSpeed}),
        dataType: "json"
    })
}