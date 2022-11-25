// Use a hashMap for linear traversal
// store target's compliment to the current number as key and index as value

const twoSum = (arr, target) => {
  const hashMap = {};
  for (let i = 0; i < arr.length; i++) {
    const num = arr[i];
    if (hashMap[num] !== undefined) {
      return [hashMap[num], i];
    } else {
      hashMap[target - num] = i;
    }
  }
};

// Test
(() => {
  console.log(twoSum([2, 7, 11, 15], 9)); //Ans: [0,1]
  console.log(twoSum([3, 2, 4], 6)); // Ans: [1,2]
  console.log(twoSum([3, 3], 6)); // Ans: [0,1]
})();
