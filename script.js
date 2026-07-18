const button = document.getElementById("generate");
const resume = document.getElementById("resume");
const download = document.getElementById("download");

button.addEventListener("click", async () => {

    const response = await fetch(
        "http://localhost:5000/generate"
    );

    const blob = await response.blob();

    const url = URL.createObjectURL(blob);

    resume.src = url + "#toolbar=0&navpanes=0&scrollbar=0";

    download.href = url;
    download.style.display = "block";
});
