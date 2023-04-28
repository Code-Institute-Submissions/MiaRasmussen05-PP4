const incrementButton = document.querySelector(".increment");
    const decrementButton = document.querySelector(".decrement");
    const inputField = document.querySelector("#quantity");

    function submitForm() {
        var form = document.getElementById("add-to-cart-form");
        var quantity = document.getElementById("quantity").value;
        form.elements["quantity"].value = quantity;
        form.submit();
    }

    incrementButton.addEventListener("click", () => {
        let currentValue = parseInt(inputField.value);

        if (currentValue < parseInt(inputField.max)) {
            inputField.value = currentValue + 1;
        }
    });

    decrementButton.addEventListener("click", () => {
        let currentValue = parseInt(inputField.value);

        if (currentValue > parseInt(inputField.min)) {
            inputField.value = currentValue - 1;
        }
    });