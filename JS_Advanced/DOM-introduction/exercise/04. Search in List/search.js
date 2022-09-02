function search() {
   let userWord = document.getElementById('searchText').value;
   let townsElements = Array.from(document.querySelectorAll('#towns li'));
   let matchesElement = document.getElementById('result');

   let count = 0;

   for (let town of townsElements) {
      if (town.textContent.includes(userWord)) {
         count++;
         town.style.fontWeight = 'bold';
         town.style.textDecoration = 'underline';
      } else {
         town.style.fontWeight = 'normal';
         town.style.textDecoration = 'none';
      }
   }
   matchesElement.textContent = `${count} matches found`
}
