// Solution 1 (Using Hashmap + PriorityQueue )
class Solution1 {
    public int[] topKFrequent(int[] nums, int k) {

        // Creating HashMap where number is key and value is frequency of number occurrence
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums){ map.put(num, map.getOrDefault(num, 0) + 1); }
        
        // Creating heap by comparing its frequency from map
        // All the keys having higher frequency will end up at start of the queue
        Queue<Integer> heap = new PriorityQueue<>((a, b) -> map.get(b) - map.get(a));
        for(int key : map.keySet()){ heap.add(key); }
        
        // Creating array of length k and adding elements
        // to array by polling from the heap k times
        int [] ans = new int [k];
        for(int i = 0; i < k; i++){
            ans[i]= heap.poll();
        }
        return ans;
    }
}