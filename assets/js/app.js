function findMatchingDrinks() {
    const selectedIngredients = Array.from(document.querySelectorAll('input[type=checkbox]:checked')).map(checkbox => checkbox.value);

    displayMatchingDrinks(selectedIngredients);
}

function displayMatchingDrinks(ingredients) {
    const resultContainer = document.getElementById('resultContainer');
    resultContainer.innerHTML = '<p>Display matched drinks here </p>';
}