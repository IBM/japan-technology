window.addEventListener('DOMContentLoaded', () => {
    checkIAMStatus();
    checkCOSStatus();
});

baseUri = location.protocol + '//' + location.host;
function checkIAMStatus() {
    iamUri = baseUri + '/status/iam';
    fetch(iamUri)
        .then(res => res.json())
        .then(data => {
            document.getElementById('iam-status').textContent = data.message;
        })
        .catch(error => {
            document.getElementById('iam-status').textContent = 'IAM check failed: ' + error;
        });
}

function checkCOSStatus() {
    cosUri = baseUri + '/status/cos';
    fetch(cosUri)
        .then(res => res.json())
        .then(data => {
            document.getElementById('cos-status').textContent = data.message;
        })
        .catch(error => {
            document.getElementById('cos-status').textContent = 'Object Storage check failed: ' + error;
        });
} 
