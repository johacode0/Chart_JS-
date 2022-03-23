$(function () {
    var $temperature = $("#temperature-graph");
    $.ajax({
        url: $temperature.data("url"),
        success: function (data) {

            var ctx = $temperature[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
                data: {
                    labels: data.data,
                    datasets: [{
                        label: 'Température',
                        backgroundColor: 'rgb(28, 67, 93)',
                        data: data.labels
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Température en fct de temps'
                    }
                }
            });

        }
    });

});

