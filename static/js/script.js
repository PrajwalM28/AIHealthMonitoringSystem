setInterval(() => {
    fetch('/predict')
        .then(response => response.json())
        .then(data => {
            document.getElementById('anomaly-status').innerText = `Anomaly Detected: ${data.is_anomaly}`;
        });
}, 2000);  // Fetch predictions every 2 seconds
