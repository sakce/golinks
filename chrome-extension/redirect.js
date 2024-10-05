function redirect(request) {
    const prefix = 'http://go/';
    const path = request.url.slice(prefix.length);
    return { redirectUrl: 'http://localhost:8000/go/' + path };
}

chrome.webRequest.onBeforeRequest.addListener(redirect, { urls: ['http://go/*']}, ['blocking']);
