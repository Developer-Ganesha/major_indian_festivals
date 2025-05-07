function updateTimer() {
    fetch('/api/timer')
        .then(response => response.json())
        .then(data => {
            const timeLeft = data.time_left;
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            document.getElementById('timer').textContent = 
                `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            
            if (timeLeft <= 0) {
                window.location.href = '/';
            }
        });
}

// Update timer every second
setInterval(updateTimer, 1000);
updateTimer(); // Initial update 