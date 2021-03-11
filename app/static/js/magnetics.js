let form = $("#config-form");
let matSelect = $("#material");
let permSelect = $("#permeability")
let currentSelectedMat = $("#material > option:selected");
let upperLimit = Math.ceil($("#oersted_plot").val());
let factors;




// -- Initial run
getPermForMat();
calculateExcitation();
createBiasDC();

// -- Event listeners
matSelect.on("click", updateMatSelection);
permSelect.on("click", getFactors);
$(".selection-entry input[type='radio']").on("click", calculateExcitation);
$(".excitation input[type='text']").on("keyup", calculateExcitation);
$(".oe-plot input[type='text']").on("keyup", updateBiasDC)

// -- named functions
function updateMatSelection() {
    let newSelected = $("#material > option:selected");
    if (currentSelectedMat.val() == newSelected.val()) {
        console.log("Selection didn't change, don't do anything");
    } else {
        console.log("New selection:" + newSelected.val());
        currentSelectedMat = newSelected;
        getPermForMat();
    }
}

function getPermForMat() {
    let path = "set_mat/" + currentSelectedMat.val();
    $.get(path, function (data) {
        $("#permeability > option").remove();
        let dataArray = JSON.parse(data);
        dataArray.forEach((e) => {
            permSelect.append('<option value="' + e + '">' + e + '</option>')
        });
        $("#permeability > option").first().attr("selected", "selected");
        getFactors();
    });

}

function getFactors() {
    let currentSelectedPerm = $("#permeability > option:selected");
    let path = "get_factors/" + currentSelectedMat.val() + "/" + currentSelectedPerm.val();
    $.get(path, function (data) {
        factors = JSON.parse(data);
        updateBiasDC();
    })
}

function calculateExcitation() {
    let dcBias = Number($("#dc_bias").val());
    let numTurns = Number($("#num_turns").val());
    let pathLength = Number($("#path_length").val());
    let exc_atcm = dcBias * numTurns / pathLength;
    let unit = $("input[name='oersted']:checked").val();
    let val = $("#calculated-excitation");
    let valUnit = $("#selected-unit");
    if (unit == undefined) {
        valUnit.html("Please select unit");
        val.html("");
    } else if (unit == "Oe") {
        valUnit.html("Oe");
        val.html(toOe(exc_atcm).toPrecision(5));
    } else if (unit = "AT/cm") {
        valUnit.html("AT/cm");
        val.html(exc_atcm.toPrecision(5));
    }
    return exc_atcm;
}

function toOe(atcm) {
    return (atcm * 4 / Math.PI);
}

function toAtcm(oe) {
    return (oe / 4 * Math.PI);
}

function updateBiasDC() {
    upperLimit = Math.ceil($("#oersted_plot").val());
    if (upperLimit == undefined) {
        upperLimit = 0;
    }
    let input = numberRange(0, upperLimit, Math.ceil(upperLimit / 40));
    let output = input.map((e) => { return (1 / (factors.perm_dc.a + factors.perm_dc.b * (e ** factors.perm_dc.c))); });
    let plotData = [{ "x": input, "y": output, "type": "scatter" }];
    // Plotly.update("graph-area", plotData, generateLayout());
    Plotly.newPlot("graph-area", plotData, generateLayout());
}

function createBiasDC() {
    upperLimit = Math.ceil($("#oersted_plot").val());
    if (upperLimit == undefined) {
        upperLimit = 0;
    }
    let input = numberRange(0, upperLimit, Math.ceil(upperLimit / 40));
    let output = input.map((e) => { return (1 / (factors.perm_dc.a + factors.perm_dc.b * (e ** factors.perm_dc.c))); });
    let plotData = [{ "x": input, "y": output, "type": "scatter" }];
    Plotly.newPlot("graph-area", plotData, generateLayout());
}

function numberRange(start, end, step) {
    return new Array(end - start).fill().map((d, i) => i * step + start);
}

function generateLayout() {
    let rangeLimitUp;
    if (upperLimit == 0) {
        rangeLimitUp = 100;
    } else {
        rangeLimitUp = upperLimit;
    }
    return {
        title: 'Permability in function of DC bias',
        plot_bgcolor: "#cccccc",
        xaxis: {
            title: 'DC bias (AT/cm)',
            showgrid: true,
            range: [0, rangeLimitUp],
            tickvals: numberRange(0, rangeLimitUp, Math.ceil(rangeLimitUp / 40))
        },
        yaxis: {
            title: 'Percent of initial permeabililty (%)',
            showline: false,
            range: [0, 105],
        }
    };
}