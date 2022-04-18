var x = document.getElementById("Ms_Scarlet");
x.style.marginTop = '-300px';

function move_img(str, pc) {
    console.log({pc});
    var step= 115;
    var pc_2 = String(pc);
    switch(str) {
        case "down":
            var x = document.getElementById(pc_2).offsetTop;
            x = x + step ;
            document.getElementById(pc_2).style.top = x + 'px';
        break;
        case "up":
            var x = document.getElementById(pc_2).offsetTop;
            x = x - step;
            document.getElementById(pc_2).style.top = x + 'px';
        break;
        case "right":
            var y = document.getElementById(pc_2).offsetLeft;
            y = y + step  ;
            document.getElementById(pc_2).style.left = y + 'px';
        break;
        case "left":
            var y = document.getElementById(pc_2).offsetLeft;
            y = y - step;
            document.getElementById(pc_2).style.left = y + 'px';
        break;
    }
}
