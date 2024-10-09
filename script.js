// Function to load quotes from the JSON file
async function loadQuotes() {
    const response = await fetch('quotes.json');  // Fetch the quotes.json file
    const quotes = await response.json();  // Parse it as JSON
    return quotes;
}

// Function to generate a random quote
async function generateQuote() {
    const quotes = await loadQuotes();  // Load quotes dynamically
    const randomIndex = Math.floor(Math.random() * quotes.length);  // Get a random index
    const selectedQuote = quotes[randomIndex];  // Select the random quote

    // Display the quote and the author on the webpage
    document.getElementById('quote').innerHTML = `"${selectedQuote.quote}"<br>— ${selectedQuote.author}`;
}
