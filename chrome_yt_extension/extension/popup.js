const btn = document.getElementById("summarise");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs) {
        var url = tabs[0].url;
        var videoId = url.split('=')[1];

        console.log(`URL in popup: ${url}`);  // Debug statement
        console.log(`Video ID in popup: ${videoId}`);  // Debug statement

        // Display URL and video ID
        const urlDisplay = document.getElementById("url");
        const videoIdDisplay = document.getElementById("video_id");
        urlDisplay.innerHTML = `URL: ${url}`;
        videoIdDisplay.innerHTML = `Video ID: ${videoId}`;

        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        xhr.onload = function() {
            console.log(`Response status: ${xhr.status}`);  // Debug statement
            if (xhr.status === 200) {
                var text = xhr.responseText;
                const p = document.getElementById("output");
                p.innerHTML = text;
            } else {
                console.error(`Error in response: ${xhr.responseText}`);  // Debug statement
            }
            btn.disabled = false;
            btn.innerHTML = "Summarise";
        };
        xhr.onerror = function() {
            console.error(`Network error`);  // Debug statement
            btn.disabled = false;
            btn.innerHTML = "Summarise";
        };
        xhr.send();
    });
});
