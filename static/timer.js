function addHours(date, hours) {
    const newDate = new Date(date);
    newDate.setHours(newDate.getHours() + hours);
    return newDate;
  }

function countdownTimeStart() {
    const date = new Date();           // Fri Feb 26 2021 20:08:30
    const newDate = addHours(date, 1); // Fri Feb 26 2021 21:08:30
    var countDownDate = newDate.getTime();

    // Update the count down every 1 second
    var x = setInterval(function () {

        // Get todays date and time
        var now = new Date().getTime();

        // Find the distance between now an the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Output the result in an element with id="demo"
        document.getElementById("button").innerHTML = "Идет поиск исполнителя...";
        document.getElementById("timer").innerHTML = "Осталось: " + minutes + ":" + seconds;

        // If the count down is over, write some text 
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("button").innerHTML = "Исполнитель найден";
            document.getElementById("timer").innerHTML = "";
        }
    }, 1000);
}