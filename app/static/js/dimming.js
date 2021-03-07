const dimElements = $(".dim-descr");
const hideButtons = $(".delete-button");

dimElements.on("click", function () {
    let path = "get_curve/" + $(this).parent().attr("name");
    $.get(path, function (data) {
        let plot_data = JSON.parse(data);
        Plotly.newPlot('plot-area', plot_data, default_layout);
    });
})

hideButtons.on("click", function () {
    let path = "delete_file/" + $(this).parent().attr("name");
    console.log(path);
    let form = $("#delete-file");
    form.attr("action", path);
    form.submit();
})