// Solution 1 (Brute Force)
class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        int[] res= new int [2];

        //Looping through the array and initializing i at zeroth index
        for(int i=0;i<nums.length-1;i++){

            // Looping again but this time initializing j at i+1 index
            for(int j=i+1;j<nums.length;j++){

                //checking if sum is equals to target
                if(nums[i]+nums[j]==target){
                    res[0]=i;
                    res[1]=j;
                    return res;
                }
            }
        }
        return res;
    }
}

// Solution 2 (Using Hashmap)
class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        
        //Creating Hashmap to store value as key and its index as value
        HashMap<Integer, Integer> map = new HashMap<>();
        
        //Storing array value and its index in map
        for(int i=0;i<nums.length;i++){
            map.put(nums[i],i);
        }

        // Looping and checking map for the remainder of current value subtracted from target
        for(int i=0;i<nums.length;i++){
            int n1=nums[i];
            int rem = target - n1;
            if(map.containsKey(target-nums[i])){

                //Getting index of the value
                int index = map.get(target-nums[i]);

                //Making sure current index in not equal to index in map
                if(index == i){
                    continue;
                }

                // returning current index and index of remainder value from the map
                return new int[]{i,index};
            }
        }

        //returning empty array if above conditions not satisfied
        return new int[]{};
    }
}