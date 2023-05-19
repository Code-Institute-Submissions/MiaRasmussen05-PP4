function sendMail(contactForm) {
    emailjs.send("service_020r79k", "template_6nngexk", {
        "to_name": "Mia Rasmussen",
        "from_fiName": contactForm.fiName.value,
        "from_laName": contactForm.laName.value,
        "from_email": contactForm.email.value,
        "for_reason": contactForm.formSelect.value,
        "inquiry_request": contactForm.teArea.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    contactForm.preventDefault();
    contactForm.target.reset();
    
    return false;
}