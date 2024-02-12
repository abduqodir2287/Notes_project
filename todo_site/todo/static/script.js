// Select all elements with the class 'counter'
const counters = document.querySelectorAll('.counter');

// Iterate over each counter element
counters.forEach(counter => {
    // Set initial text content of the counter to '0'
    counter.innerText = '0';

    // Define a function to update the counter
    const updateCounter = () => {
        // Get the target value from the 'data-target' attribute
        const target = +counter.getAttribute('data-target');

        // Get the current value of the counter
        const current = +counter.innerText;

        // Calculate the increment value based on the target
        const increment = target / 200;

        // Check if the current value is less than the target
        if (current < target) {
            // Update the counter text content with the incremented value
            counter.innerText = ${Math.ceil(current + increment)};

            // Schedule the next update using setTimeout
            setTimeout(updateCounter, 1);
        } else {
            // If the target is reached, set the counter text content to the target value
            counter.innerText = target;
        }
    };

    // Trigger the initial updateCounter function
    updateCounter();
});