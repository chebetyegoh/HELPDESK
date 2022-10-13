var ctx = document.getElementById('myChart').getContext('2d');
var myChart2 = document.getElementById('myChart2').getContext('2d');
var myChart3 = document.getElementById('myChart3').getContext('2d');



var myChart = new Chart(ctx, {
    type: 'polarArea',
    data: {
        labels: ['Open Tickets','Closed Tickets'],
        datasets: [{
            label: 'Tickets Resolution',
            data: [8, 5],
            backgroundColor: [
                '#CD0046',
                '#130170',
                // '#01949A'
            ],
        }]
    },
    options: {
       responsive: true,
    }
});

var myChart = new Chart(myChart3, {
    type: 'bar',
    data: {
        labels: ['Open Tickets','Closed Tickets'],
        datasets: [{
            label: 'Ticket Resolution',
            data: [8, 5],
            backgroundColor: [
                '#CD0046',
                '#130170',
                // '#01949A'
            ],
        }]
    },
    options: {
        response:true,
    }
});

var myChart = new Chart(myChart2, {
    type: 'line',
    data: {
        labels: ['Open Tickets', 'Closed Tickets'],
        datasets: [{
            label: 'Ticket Resolution',
            data: [8, 5],
            backgroundColor: [
                '#CD0046',
                '#130170',
                // '#01949A'
            ],
        }]
    },
    options: {
        response:true,
    }
});

