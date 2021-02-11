const SaveButton = document.querySelector("#save_db");
const DelButton = document.querySelector("#delete_db");

// -- Eventlisteners:
SaveButton.addEventListener("click", () => {
    document.querySelector("#param-form").submit();
})
