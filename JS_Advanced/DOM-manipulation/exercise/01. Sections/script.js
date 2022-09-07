function create(words) {
   let contentElement = document.getElementById('content');

   words.forEach(element => {
      let pElement = document.createElement('p');
      pElement.style.display = 'none';
      let divElement = document.createElement('div');

      pElement.textContent = element;
      divElement.appendChild(pElement);

      divElement.addEventListener('click', () => {
         pElement.style.removeProperty('display');
      })

      contentElement.appendChild(divElement);
   });
}