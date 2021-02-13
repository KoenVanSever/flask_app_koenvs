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


// -- Named functions:
function makeDimmingCurve(input) {
    let i = 0;
    let reference = document.getElementById("Dimming Curve 6600 mA").value;
    for (e of dcBytes) {
        document.getElementById(e).value = Math.round(input[i] * reference / 100);
        i += 1;
    }
}


