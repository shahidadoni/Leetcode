// Approach 1 - brute force
const containsDuplicate1 = (nums) => {
  // return false by default
  // only return true if there is a repetition

  //   step 1: construct freq hash map
  const freqMap = {};

  nums.map((num) => {
    if (freqMap[num]) {
      freqMap[num] += 1;
    } else {
      freqMap[num] = 1;
    }
  });

  //   if any of the freq is more than 1 -> return true
  const keys = Object.keys(freqMap);
  for (let i = 0; i < keys.length; i++) {
    if (freqMap[keys[i]] && freqMap[keys[i]] > 1) {
      return true;
    }
  }

  return false;
};

// Approach 2 - using a single loop
const containsDuplicate2 = (nums) => {
  const freqMap = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];

    if (freqMap[num]) {
      return true;
    } else {
      freqMap[num] = 1;
    }
  }
  return false;
};

// Approach 3 - using built-in set data structure => that's cheating i guess lol 😂
const containsDuplicate3 = (nums) => {
  const set = new Set(nums);
  return nums.length !== set.size;
};

// Testing - IIFE's are cool!
(() => {
  // Approach 1
  console.log(containsDuplicate1([1, 2, 3, 1]) === true);
  console.log(containsDuplicate1([1, 2, 3, 4]) === false);
  console.log(containsDuplicate1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) === true);

  console.log("--------------------------------");

  // Approach 2
  console.log(containsDuplicate2([1, 2, 3, 1]) === true);
  console.log(containsDuplicate2([1, 2, 3, 4]) === false);
  console.log(containsDuplicate2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) === true);

  console.log("--------------------------------");

  // Approach 3
  console.log(containsDuplicate3([1, 2, 3, 1]) === true);
  console.log(containsDuplicate3([1, 2, 3, 4]) === false);
  console.log(containsDuplicate3([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) === true);
})();
