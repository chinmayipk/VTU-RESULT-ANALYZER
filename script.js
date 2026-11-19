// Search validation
function validateSearch() {
    const input = document.querySelector(
        'input[name="usn"]'
    );

    if (!input.value.trim()) {
        alert("Please enter Student USN");
        return false;
    }

    return true;
}

// Highlight table rows
document.querySelectorAll("tbody tr").forEach(row => {
    row.addEventListener("click", () => {
        row.style.backgroundColor = "#dbeafe";
    });
});

// Welcome message
console.log("VTU Result Analyzer Frontend Loaded!");
