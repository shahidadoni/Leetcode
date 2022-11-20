
// Solution 1 (Naive Approach)
//     This solution passes all test cases but exceeds timelimit
class Solution1a {
    public boolean containsDuplicate(int[] nums) {
        // brute force two pointer traversing using two loops
        for(int i = 0; i < nums.length; i++){
            //initializing i at zeroth index
            for(int j=i+1; j<nums.length;j++ ){
                //initializing j at i+1th index
                if(nums[i]==nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}

class Solution1b {
    public boolean containsDuplicate(int[] nums) {
        // Two pointer using two loops i at first index and j at last index
        for(int i = 0; i < nums.length; i++){
            //initializing i at zeroth index
            for(int j=nums.length-1; j>i; j-- ){
                //initializing j last index of array and 
                // decrementing j till we reach i+1 index
                if(nums[i]==nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}

// Solution 2 (Intermediate approach)
class Solution2 {
    public boolean containsDuplicate(int[] nums) {
        // Sorting methods using Arrays.sort and checking the 
        // immediate next element returning true if same.
        Arrays.sort(nums);
        for(int i=0; i < nums.length-1; i++){
            if(nums[i]==nums[i+1]){
                return true;
            }
        }
        return false;
    }
} 

// Solution 3 (best approach)
// Using HashSet and checking for the value in hashset 
// if doesn't exists adding value into the hashset
class Solution3 {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i=0; i < nums.length; i++){
            if(set.contains(nums[i])){
                return true;
            }else{
                set.add(nums[i]);
            }
        }
        return false;
    }
}