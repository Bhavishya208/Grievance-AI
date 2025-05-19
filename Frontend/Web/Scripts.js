document.getElementById('complaintForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const complaintData = {
        category: event.target.category.value,
        description: event.target.description.value,
        location: event.target.location.value
    };
    fetch('/complaints', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(complaintData)
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
});
