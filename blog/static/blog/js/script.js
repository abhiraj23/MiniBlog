// custom.js

document.addEventListener('DOMContentLoaded', function() {
    var alerts = document.querySelectorAll('.alert');

    alerts.forEach(function(alert) {
        // Check if the alert has the 'auto-dismiss' class
        if (alert.classList.contains('auto-dismiss')) {
            // Automatically close the alert after 1 second
            setTimeout(function() {
                alert.classList.add('fade');
                setTimeout(function() {
                    alert.remove();
                }, 1000); // Change timeout to 1000 milliseconds (1 second)
            }, 1000); // Change timeout to 1000 milliseconds (1 second)
        }
    });
});
