var x = document.getElementById("Ms_Scarlet");
x.style.marginTop = '-300px';

function move_img(str,pc) {
    console.log({pc});
    var step = 50;
    var pc_2 = {pc};
    switch(str) {
        case "down":
            var x = document.getElementById('Col_Mustard').offsetTop;
            x = x + step;
            document.getElementById('Col_Mustard').style.top = x + 'px';
        break;
        case "up":
            var x = document.getElementById('Col_Mustard').offsetTop;
            x = x - step;
            document.getElementById('Col_Mustard').style.top = x + 'px';
        break;
        case "right":
            var y = document.getElementById('Col_Mustard').offsetLeft;
            y = y + step;
            document.getElementById('Col_Mustard').style.left = y + 'px';
        break;
        case "left":
            var y = document.getElementById({pc_2}).offsetLeft;
            y = y - step;
            document.getElementById({pc_2}).style.left = y + 'px';
        break;



    }
}
