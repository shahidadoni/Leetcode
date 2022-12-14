/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  // check rows
  for (let i = 0; i < 9; i++) {
    const chars = board[i];
    const isValid = isEveryCharacterUnique(chars);
    if (!isValid) {
      return false;
    }
  }

  console.log("Rows are valid");

  // check columns
  for (let i = 0; i < 9; i++) {
    const chars = [];
    for (let j = 0; j < 9; j++) {
      chars.push(board[j][i]);
    }
    const isValid = isEveryCharacterUnique(chars);
    if (!isValid) {
      return false;
    }
  }

  console.log("Columns are valid");

  // check 3x3 boxes
  for (let i = 0; i < 9; i += 3) {
    for (let j = 0; j < 9; j += 3) {
      const chars = [
        board[i][j],
        board[i][j + 1],
        board[i][j + 2],

        board[i + 1][j],
        board[i + 1][j + 1],
        board[i + 1][j + 2],

        board[i + 2][j],
        board[i + 2][j + 1],
        board[i + 2][j + 2],
      ];
      console.log(chars);
      const isValid = isEveryCharacterUnique(chars);
      if (!isValid) {
        return false;
      }
    }
  }

  console.log("3x3 boxes are valid");

  return true;
};

function isEveryCharacterUnique(arrOfChars) {
  // clean dots
  let cleanedArr = arrOfChars.filter((char) => char !== ".");

  const set = new Set(cleanedArr);
  return cleanedArr.length === set.size;
}

(() => {
  //   const chars = ["8", "3", "1", "2", "7", "9", "5", "4", "6"];
  //   const chars2 = ["8", "3", ".", ".", "7", ".", ".", ".", "."];
  //   console.log(isEveryCharacterUnique(chars));
  //   console.log(isEveryCharacterUnique(chars2));

  const board1 = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
  ];

  console.log(isValidSudoku(board1));
})();
