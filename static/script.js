document.addEventListener("DOMContentLoaded", function () {
    const envelope = document.getElementById("envelope");
    const envelopeSection = document.getElementById("envelope-section");
    const mainContent = document.getElementById("main-content");

    envelope.addEventListener("click", function () {
        envelopeSection.style.display = "none";
        mainContent.classList.remove("hidden");
    });
});