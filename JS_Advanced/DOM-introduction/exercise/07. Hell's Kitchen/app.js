function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);
   

   function onClick() {
      let input = JSON.parse(document.querySelector('#inputs textarea').value);

      let avgSalary = 0;
      let totalSalary = 0;
      let maxAvgSalary = 0;
      let bestName = '';
      let output = {};

      for (let line of input) {
         let [restName, workersInfo] = line.split(' - ');
         let workers = workersInfo.split(', ');

         let currTotalSalary = 0;
         for (let worker of workers) {
            let [workerName, workerSalary] = worker.split(' ');
            if (!output.hasOwnProperty(restName)) {
               output[restName] = {};
            }
            output[restName][workerName] = Number(workerSalary);
         }

      }
      let entries = Object.entries(output);

      for (let entry of entries) {
         let key = entry[0];
         let values = Object.values(entry[1]);

         for (let salary of values) {
            totalSalary += salary;
         }
         avgSalary = totalSalary / values.length;
         if (avgSalary > maxAvgSalary) {
            maxAvgSalary = avgSalary;
            bestName = key;
            totalSalary = 0;
         }
      }
      let result = Object.entries(output[bestName]).sort((a, b) => b[1] - a[1]);

      let print = '';

      result.forEach(w => print += `Name: ${w[0]} With Salary: ${w[1]} `);

      document.querySelector('#bestRestaurant p').textContent = `Name: ${bestName} Average Salary: ${maxAvgSalary.toFixed(2)} Best Salary: ${result[0][1].toFixed(2)}`;
      document.querySelector('#workers p').textContent = print;
   }
}