const defaultWhite = [0, 0.41, 1.00, 5.60, 14.00, 24.00, 33.50, 100.00];
const dcBytes = ["Dimming Curve 1400 mA", "Dimming Curve 2800 mA", "Dimming Curve 3400 mA", "Dimming Curve 4100 mA", "Dimming Curve 4800 mA", "Dimming Curve 5200 mA", "Dimming Curve 5500 mA", "Dimming Curve 6600 mA"];
const defaultColor = [0, 0.85, 2.00, 7.20, 14.00, 27.60, 40.00, 100.00];
const fluxBytes = ["Flux Compensation (-25 °C)", "Flux Compensation (0 °C)", "Flux Compensation (25 °C)", "Flux Compensation (50 °C)", "Flux Compensation (75 °C)", "Flux Compensation (Max °C)"];

const fluxInput = document.querySelector("#flux-input");
const fluxButton = document.querySelector("#set-flux");
const saveButton = document.querySelector("#save_db");
const dcWhite = document.querySelector("#dc-white");
const dcColor = document.querySelector("#dc-color");

// -- Eventlisteners:
saveButton.addEventListener("click", () => {
    document.querySelector("#param-form").submit();
});
dcWhite.addEventListener("click", () => {
    makeDimmingCurve(defaultWhite);
})
dcColor.addEventListener("click", () => {
    makeDimmingCurve(defaultColor);
})
fluxButton.addEventListener("click", () => {
    let target = fluxInput.value;
    for (element of fluxBytes) {
        document.getElementById(element).value = target;
    }
})
// -- Error check coloring
// /i used with jQuery
// TODO: color code inputs where flux/current/data/... match what is expected
const nomCurr = $("input[name='Nominal Current (mA)']");
const curr6600 = $("input[name='Dimming Curve 6600 mA']");
const vol1b = $("input[name='Nominal Voltage (100 mV)']");
const vol2b = $("input[name='Nominal Voltage (10 mV)']");
const numLeds = $("input[name='Number of LEDs']");
const linDim = $("input[name='Minimum Linear Dimming']");

let compareCurrent = (function (obj1, obj2) {
    if (obj1[0].value == obj2[0].value) {
        obj1.css({ "border-color": "green", "border-width": "0.3rem" });
        obj2.css({ "border-color": "green", "border-width": "0.3rem" });
    } else {
        obj1.css({ "border-color": "red", "border-width": "0.3rem" });
        obj2.css({ "border-color": "red", "border-width": "0.3rem" });
    }
});

let compareFlux = (function () {
    let array = flux.map(function () { return $(this).val() }).get();
    if (array.every((e) => { return e == array[0]; })) {
        flux.css({ "border-color": "green", "border-width": "0.3rem" });
    } else {
        flux.css({ "border-color": "red", "border-width": "0.3rem" });
    }
});

let compareVoltage = (function () {
    switch (true) {
        case (vol1b.val() < 255 && vol2b.val() == 65535):
            if (numLeds.val() * 18 < vol1b.val() && vol1b.val() < numLeds.val() * 36) {
                vol1b.css({ "border-color": "green", "border-width": "0.3rem" });
                vol2b.css({ "border-color": "green", "border-width": "0.3rem" });
                numLeds.css({ "border-color": "green", "border-width": "0.3rem" });
            } else {
                vol1b.css({ "border-color": "red", "border-width": "0.3rem" });
                vol2b.css({ "border-color": "green", "border-width": "0.3rem" });
                numLeds.css({ "border-color": "red", "border-width": "0.3rem" });
            }
            break;
        case (vol1b.val() == 255 && 2500 < vol2b.val() < 65535):
            console.log("test2");
            if (numLeds.val() * 200 < vol2b.val() && vol2b.val() < numLeds.val() * 360) {
                vol1b.css({ "border-color": "green", "border-width": "0.3rem" });
                vol2b.css({ "border-color": "green", "border-width": "0.3rem" });
                numLeds.css({ "border-color": "green", "border-width": "0.3rem" });
            } else {
                vol1b.css({ "border-color": "green", "border-width": "0.3rem" });
                vol2b.css({ "border-color": "red", "border-width": "0.3rem" });
                numLeds.css({ "border-color": "red", "border-width": "0.3rem" });
            }
            break;
        default:
            vol1b.css({ "border-color": "red", "border-width": "0.3rem" });
            vol2b.css({ "border-color": "red", "border-width": "0.3rem" });
            numLeds.css({ "border-color": "red", "border-width": "0.3rem" });
            break;
    }
});

let compareLinDim = (function () {
    if (linDim.val() < 300) {
        linDim.css({ "border-color": "yellow", "border-width": "0.3rem" });
    } else if (linDim.val() > 65535) {
        linDim.css({ "border-color": "red", "border-width": "0.3rem" });
    } else {
        linDim.css({ "border-color": "green", "border-width": "0.3rem" });
    }
});

compareLinDim();
linDim.on("keyup", () => compareLinDim());

compareCurrent(nomCurr, curr6600);
nomCurr.on("keyup", () => compareCurrent(nomCurr, curr6600));
curr6600.on("keyup", () => compareCurrent(nomCurr, curr6600));

const flux = $("input[name*='Flux Compen']");
compareFlux();
flux.on("keyup", () => compareFlux());

compareVoltage()
vol1b.on("keyup", () => compareVoltage());
vol2b.on("keyup", () => compareVoltage());
numLeds.on("keyup", () => compareVoltage());

const today = new Date();
$("#release_today").on("click", () => {
    let year = today.getFullYear();
    let week = ISO8601_week_no(today);
    $("input[name='Release Year']").val(String(year - 2000));
    $("input[name='Inverse Release Year']").val(String(255 - (year - 2000)));
    $("input[name='Release Week']").val(String(week));
    $("input[name='Inverse Release Week']").val(String(255 - week));
    $("input[name='Release Version']").val("1");
    $("input[name='Inverse Release Version']").val("254");
    $("input[name='Release Not Used']").val("1");
    $("input[name='Inverse Release Not Used']").val("254");
});
$("#prog_today").on("click", () => {
    let [month, day, year] = today.toLocaleDateString().split("/");
    let [hour, minute, second] = today.toLocaleTimeString().slice(0, 7).split(":");
    $("input[name='Programming Date Year']").val(year.substring(year.length - 2, year.length));
    $("input[name='Programming Date Month']").val(month);
    $("input[name='Programming Date Day']").val(day);
    $("input[name='Programming Date Hour']").val(hour);
})


// -- Named functions:
function makeDimmingCurve(input) {
    let i = 0;
    let reference = document.getElementById("Dimming Curve 6600 mA").value;
    for (e of dcBytes) {
        document.getElementById(e).value = Math.round(input[i] * reference / 100);
        i += 1;
    }
}

function ISO8601_week_no(dt) {
    let tdt = new Date(dt.valueOf());
    let dayn = (dt.getDay() + 6) % 7;
    tdt.setDate(tdt.getDate() - dayn + 3);
    let firstThursday = tdt.valueOf();
    tdt.setMonth(0, 1);
    if (tdt.getDay() !== 4) {
        tdt.setMonth(0, 1 + ((4 - tdt.getDay()) + 7) % 7);
    }
    return 1 + Math.ceil((firstThursday - tdt) / 604800000);
}


