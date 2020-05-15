var pi;
var digits;
var index = 0;
var resultTxt;

function preload(){
    pi = loadStrings("pi-1million.txt");
    e = loadStrings("e-10thousand.txt")
}

function setup(){
    createCanvas(600,600)
    noLoop();
    
    button = createButton('Start');
    button.position(19, 19);
    button.mousePressed(start_btn);

    button = createButton('Stop');
    button.position(19, 50);
    button.mousePressed(stop_btn);

    plot_label();

    const sdigits = pi[0].split('');
    digits = int(sdigits);
    console.log(digits)
    
    background(0)
    stroke(255);
    noFill();
    translate(width / 2, height / 2);
    ellipse(0, 0, 500, 500);
}

num_color_dict = {
    0 : "#006666",
    1 : "#0066CC",
    2 : "#330099",
    3 : "#660099",
    4 : "#990033",
    5 : "#FF3300",
    6 : "#FF9900",
    7 : "#FFFF00",
    8 : "#669933",
    9 : "#00FF00",
}

function start_btn(){
    loop();
}

function stop_btn(){
    noLoop();
}

function plot_label(){
    num_label = createP('1')
    num_label.position(520,420)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[1]);
    num_label.html(1);

    num_label = createP('4')
    num_label.position(80,420)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[4]);
    num_label.html(4);

    num_label = createP('6')
    num_label.position(80,100)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[6]);
    num_label.html(6);

    num_label = createP('9')
    num_label.position(520,100)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[9]);
    num_label.html(9);

    num_label = createP('5')
    num_label.position(30,250)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[5]);
    num_label.html(5);

    num_label = createP('0')
    num_label.position(570,250)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[0]);
    num_label.html(0);

    num_label = createP('2')
    num_label.position(380,520)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[2]);
    num_label.html(2);

    num_label = createP('8')
    num_label.position(380,10)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[8]);
    num_label.html(8);

    num_label = createP('7')
    num_label.position(225,10)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[7]);
    num_label.html(7);

    num_label = createP('3')
    num_label.position(225,520)
    num_label.style('font-size','20pt');
    num_label.style('color', num_color_dict[3]);
    num_label.html(3);

    pi_label = createP('pi')
    pi_label.position(300,240)
    pi_label.style('font-size','30pt');
    pi_label.style('color', 'White');
    pi_label.html('π');
}

function draw(){
    translate(width / 2, height / 2);

    const pi_digit = digits[index];
    const pi_nextdigit = digits[index+1]
    index++;
    //print(index)

    var rand = TWO_PI/20

    var angle1 = map(pi_digit, 0, 10, 0, TWO_PI) + random(-0.001,0.199999999);
    var xpos1 = 250*cos(angle1);
    var ypos1 = 250*sin(angle1);
    var angle2 = map(pi_nextdigit, 0, 10, 0, TWO_PI) + random(-0.001,0.199999999);
    var xpos2 = 250*cos(angle2);
    var ypos2 = 250*sin(angle2);

    if(index == 1){
        resultTxt = createP('');
    }
    resultTxt.style('font-size','20pt');
    resultTxt.html(`Number of PI digits: ${index}`);


    stroke(num_color_dict[pi_digit]);
    print(xpos1, ypos1, xpos2, ypos2)
    line(xpos1, ypos1, xpos2, ypos2);

}

