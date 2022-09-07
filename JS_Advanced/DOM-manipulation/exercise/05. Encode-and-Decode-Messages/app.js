function encodeAndDecodeMessages() {
    let givenMessageElement = document.querySelector('textarea[placeholder="Write your message here..."]');
    let receivedMessageElement = document.querySelector('textarea[placeholder="No messages..."]');

    let encodeButton = document.querySelector('div > button');
    let decodeButton = document.querySelector('#main > div:nth-child(2) > button');

    encodeButton.addEventListener('click', () => {
        let givenText = givenMessageElement.value;
        let encodedMessage = '';
        for (let i = 0; i < givenText.length; i++) {
            let currentCharCode = givenText.charCodeAt(i);
            let newChar = String.fromCharCode(currentCharCode + 1);
            encodedMessage += newChar;
        }
        receivedMessageElement.value = encodedMessage;
        givenMessageElement.value = '';
    })

    decodeButton.addEventListener('click', () => {
        let receivedText = receivedMessageElement.value;
        let decodedMessage = '';
        for (let i = 0; i < receivedText.length; i++) {
            let currentCharCode = receivedText.charCodeAt(i);
            let newChar = String.fromCharCode(currentCharCode - 1);
            decodedMessage += newChar;
        }
        receivedMessageElement.value = decodedMessage;
    })
}