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

let compareCurrent = (function (obj1, obj2) {
    if (obj1[0].value == obj2[0].value) {
        obj1.css({ "border-color": "green", "border-width": "0.2rem" });
        obj2.css({ "border-color": "green", "border-width": "0.2rem" });
    } else {
        obj1.css({ "border-color": "red", "border-width": "0.2rem" });
        obj2.css({ "border-color": "red", "border-width": "0.2rem" });
    }
});

let compareFlux = (function () {
    let array = flux.map(function () { return $(this).val() }).get();
    if (array.every((e) => { return e == array[0]; })) {
        flux.css({ "border-color": "green", "border-width": "0.2rem" });
    } else {
        flux.css({ "border-color": "red", "border-width": "0.2rem" });
    }
});

let compareVoltage = (function () {
    if ((vol1b.val() < 255 && vol2b.val() == 65535) || (vol1b.val() == 255 && vol2b.val() > 2500)) {
        vol1b.css({ "border-color": "green", "border-width": "0.2rem" });
        vol2b.css({ "border-color": "green", "border-width": "0.2rem" });
    } else {
        vol1b.css({ "border-color": "red", "border-width": "0.2rem" });
        vol2b.css({ "border-color": "red", "border-width": "0.2rem" });
    }
});

compareCurrent(nomCurr, curr6600);
nomCurr.on("keyup", () => compareCurrent(nomCurr, curr6600));
curr6600.on("keyup", () => compareCurrent(nomCurr, curr6600));

const flux = $("input[name*='Flux Compen']");
compareFlux();
flux.on("keyup", () => compareFlux());

compareVoltage()
vol1b.on("keyup", () => compareVoltage());
vol2b.on("keyup", () => compareVoltage());


// -- Named functions:
function makeDimmingCurve(input) {
    let i = 0;
    let reference = document.getElementById("Dimming Curve 6600 mA").value;
    for (e of dcBytes) {
        document.getElementById(e).value = Math.round(input[i] * reference / 100);
        i += 1;
    }
}


