function focused() {
    let mainDiv = document.getElementsByTagName("div")[0];
    let divArray = Array.from(mainDiv.getElementsByTagName('input'));
    
    divArray.forEach(element => {
        element.addEventListener("focus", focus);
    });

    divArray.forEach(element => {
        element.addEventListener("blur", focusLost);
    });


    function focus(e) {
        let parent = e.target.parentNode;
        parent.classList.add("focused");
    }

    function focusLost(e) {
        let parent = e.target.parentNode;
        parent.classList.remove("focused");
    }

}