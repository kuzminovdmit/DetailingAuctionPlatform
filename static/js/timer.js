function addHours(date, minutes) {
    const newDate = new Date(date);
    newDate.setMinutes(newDate.getMinutes() + minutes);
    return newDate;
}

function countdownTimeStart() {
    const date = new Date('{{ auction.timer_start.isoformat }}');
    const newDate = addHours(date, 2);
    var countDownDate = newDate.getTime();

    var x = setInterval(function () {
        var now = new Date().getTime();
        var distance = countDownDate - now;
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.getElementById("button").innerHTML = "Идет поиск исполнителя...";
        document.getElementById("timer").innerHTML = "Осталось: " + minutes + ":" + seconds;

        if (distance < 0) {
            clearInterval(x);
            document.getElementById("button").innerHTML = "Исполнитель найден";
            document.getElementById("timer").innerHTML = "";
            location.reload();
        }
    }, 1000);
}