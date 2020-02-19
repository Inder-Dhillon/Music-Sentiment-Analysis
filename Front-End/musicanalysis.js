var mood
function fun1() {
    mood = "h"
}

function fun2() {
    mood = "s"
}

function check(num) {
    var title;

    switch (num) {
    case 1: title = "Pop"
        break;
    case 2: title = "Rock"
    break;
    case 3:title = "Jazz"
    break;
    case 4: title = "Metal"
    break;
    case 5:title = "Reggae"
    break;
    case 6:title = "rap"
    break;
    default:
        break;
    }
    var data = $.get("https://api.spotify.com/v1/browse/categories%22,headers=%7B%22Authorization");
    console.log(data);
}
