const searchHeader = document.querySelector("#search-header");
const searchChildren = searchHeader.children;
const rows = document.querySelectorAll(".tr-data");
const filterButton = document.querySelector("#filter-button");

filterButton.addEventListener("click", toggle_hide_on_search)

function toggle_hide_on_search() {
    for (line of rows) {
        line.hidden = false;
    }
    for (e in searchChildren) {
        if (!isNaN(e)) {
            if (searchChildren[e].lastChild.value == "") {
                continue;
            } else {
                for (line of rows) {
                    if (!line.children[e].innerHTML.includes(searchChildren[e].lastChild.value)) {
                        line.hidden = true;
                    } else {
                        line.hidden = false;
                    }
                }
            }
        }
    }
}
