// If character count is same - then we can say its an anagram
const isValidAnagram = (s1, s2) => {
  const freq1 = charFreqGenerator(s1);
  const freq2 = charFreqGenerator(s2);

  return isSame(freq1, freq2);
};

// Create freq map of characters in the given string
const charFreqGenerator = (s) => {
  const freq = {};
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (freq[char] === undefined) {
      freq[char] = 1;
    } else {
      freq[char] += 1;
    }
  }
  return freq;
};

// Deep comparison of objects
const isSame = (obj1, obj2) => {
  const keys1 = Object.keys(obj1);

  for (let i = 0; i < keys1.length; i++) {
    const key = keys1[i];

    // if value for corresponding key not equal
    if (obj1[key] !== obj2[key]) {
      return false;
    }

    // delete corresponding key/value from obj2
    delete obj2[key];
  }

  //   if there are still keys left in obj2 - return false
  if (Object.keys(obj2).length !== 0) {
    return false;
  }

  return true;
};

// Test
(() => {
  console.log(isValidAnagram("anagram", "nagaram") === true);
  console.log(isValidAnagram("rat", "car") === false);
})();
