const isValidAnagram = require("../../242. Valid Anagram/abhi/validAnagram");

// Brute force approach - O(n^2)
// Compare every pair and see if they are valid anagrams
const solution1 = (strs) => {
  const len = strs.length;

  // For elements which are already added into a group, we should ignore them
  const alreadyCoveredIndexes = {};
  const res = [];

  for (let i = 0; i < len; i++) {
    const group = [];

    // if the curr element is already an anagram with anything previously
    // we don't have to compare it with the rest
    if (alreadyCoveredIndexes[i] === undefined) {
      group.push(strs[i]);
    } else {
      continue;
    }

    for (let j = i + 1; j < len; j++) {
      const areAnagrams = isValidAnagram(strs[i], strs[j]);
      if (areAnagrams) {
        group.push(strs[j]);
        alreadyCoveredIndexes[j] = true;
      }
    }

    res.push(group);
  }

  return res;
};

// Test
(() => {
  const strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"];
  console.log(solution1(strs1));
  //   Ans: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]];

  const strs2 = [""];
  console.log(solution1(strs2));
  //   Ans: [[""]];

  const strs3 = ["a"];
  console.log(solution1(strs3));
  //   Ans: [["a"]];
})();
