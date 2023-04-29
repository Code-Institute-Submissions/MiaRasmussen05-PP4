const incrementButton = document.querySelector(".increment");
const decrementButton = document.querySelector(".decrement");
const inputField = document.querySelector("#quantity");

const incrementQuntityButtons = document.querySelectorAll(".increment");
const decrementQuntityButtons = document.querySelectorAll(".decrement");

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


incrementQuntityButtons.forEach((button) => {
    button.addEventListener("click", () => {
        let currentItem = button.parentElement.querySelector("[data-cart-item-id]");
        let currentValue = parseInt(currentItem.value);

        if (currentValue < parseInt(currentItem.max)) {
            currentItem.value = currentValue + 1;
        }
    });
});

decrementQuntityButtons.forEach((button) => {
    button.addEventListener("click", () => {
        let currentItem = button.parentElement.querySelector("[data-cart-item-id]");
        let currentValue = parseInt(currentItem.value);

        if (currentValue > parseInt(currentItem.min)) {
            currentItem.value = currentValue - 1;
        }
    });
});