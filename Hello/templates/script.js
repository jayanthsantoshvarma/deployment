function displayImage(event) {
    let reader = new FileReader();
    reader.onload = function(){
        let output = document.getElementById('uploaded-image');
        output.src = reader.result;
        let predictButton = document.getElementById("predict-btn");
        predictButton.classList.toggle("d-none")
        predictButton.classList.toggle("text-right")
    };
    reader.readAsDataURL(event.target.files[0]);
}

let spinnerElmt = document.getElementById("spinner")

let startPredicting = () => {
    spinnerElmt.classList.toggle("spinner")
}