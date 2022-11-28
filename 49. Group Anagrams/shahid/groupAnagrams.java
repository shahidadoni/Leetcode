// Using Hashmap to store hash of a string and 
//checking the string hash value in map and adding the string 
// in a list as a value of the hash key in map

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>>mp=new HashMap<>();
        
        for(String s: strs){
            List<String> tmp=mp.getOrDefault(sortString(s),new ArrayList()); 
            tmp.add(s);
            mp.put(sortString(s),tmp);
        }
        return new ArrayList<>(mp.values());
    }
    
     String sortString(String inputString)
    {
        char tempArray[] = inputString.toCharArray();
          
        Arrays.sort(tempArray);
          
        return new String(tempArray);
    }
}