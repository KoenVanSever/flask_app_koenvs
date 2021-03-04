const dimElements = $(".dim-element");

dimElements.on("click", function () {
    let path = "get_curve/" + $(this).attr("name");
    $.get(path, function (data) {
        let plot_data = JSON.parse(data);
        Plotly.newPlot('plot-area', plot_data, default_layout);
    });
})