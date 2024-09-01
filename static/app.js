let sesn = [];

document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('sub-btn');
    button.addEventListener('click', async () => {
        const inputval = document.getElementById('chat').value;
        if (inputval.trim() === '') return; // Prevent adding empty messages

        // Add user message to UI and array
        sesn.push(inputval);
        const messageContainer = document.querySelector('.message-container');
        
        const userMessageElement = document.createElement('div');
        userMessageElement.classList.add('message');
        userMessageElement.textContent = `You: ${inputval}`;
        messageContainer.appendChild(userMessageElement);

        // Clear the input field
        document.getElementById('chat').value = '';

        // Send the message to the Express backend
        try {
            const response = await fetch('http://localhost:5000/message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: inputval }),
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const responseData = await response.json();
            console.log(responseData);

            // Add response message to UI and array
            sesn.push(responseData.response);

            const responseMessageElement = document.createElement('div');
            responseMessageElement.classList.add('message');
            responseMessageElement.textContent = `Server: ${responseData.response}`;
            messageContainer.appendChild(responseMessageElement);

        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
        console.log(sesn)
    });
});
