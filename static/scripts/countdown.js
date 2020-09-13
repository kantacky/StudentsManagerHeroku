var endDate = new Date('2021/01/16 09:30:00');
var interval = 1000;

function countdown() {
    var nowDate = new Date();
    var period = endDate - nowDate;
    var addZero = function(n) { return ('0' + n).slice(-2); }
    var addZeroDay = function(n) { return ('0' + n).slice(-3); }
    if (period >= 0) {
        var day = Math.floor(period / (1000 * 60 * 60 * 24));
        period -= (day　 * (1000 * 60 * 60 * 24));
        var hour = Math.floor(period / (1000 * 60 * 60));
        period -= (hour * (1000 * 60 * 60));
        var minutes = Math.floor(period / (1000 * 60));
        period -= (minutes * (1000 * 60));
        var second = Math.floor(period / 1000);
        var insert = "";
        insert += addZeroDay(day) + ' days ';
        insert += addZero(hour) + ' hours ';
        insert += addZero(minutes) + ' mins ';
        insert += addZero(second) + ' secs ';
        document.getElementById('result').innerHTML = insert;
        setTimeout(countdownTimer, 10);
    } else {
        var insert = "";
        var number = 0;
        insert += number + number;
        insert += number + number;
        insert += number + number;
        document.getElementById('countdown').innerHTML = insert;
    }
}

countdown();