//Solution 1 (Naive Approach)

    // Iterating through 1st string and 2nd string inside first loop
    // making position of character from 1st string as 0 in 2nd string
    // Doing this till we find no matching character in 2nd string and returning false
    // else true

//Solution 2 (Sorting Approach)
    
    //Sorting the strings and checking if they are same

//Solution 3 (Using Array as ASCII values of alphabet)
    // This is solution does not works for non-english letters or symbols

class Solution3 {
    public boolean isAnagram(String s, String t) {
        // returning false is string length is not same
        if(s.length() != t.length()){
            return false;
        }

        //Creating a alphabet frequency array 
        //American Standard Code for Information Interchange(ASCII) array
        int charFrequencyArr[] = new int[26];

        for(int i=0; i<s.length();i++){

            // incrementing value by 1 at index of array which 
            //represents the ASCII value of the letter in 1st string
            charFrequencyArr[s.charAt(i)-'a']++;

            // Decrementing value for the letter in 2nd string
            charFrequencyArr[t.charAt(i)-'a']--;
        }

        //Checking for all elements of arrays if not zero returning false
        for(int i=0; i<charFrequencyArr.length;i++){
            if(charFrequencyArr[i]!=0){
                return false;
            }
        }
        return true;
    }
}

// Solution 4 (Using HashMap)
    // This solution works for follow up question 
    //i.e. non-english letters or symbols

class Solution4a {
    public boolean isAnagram(String s, String t) {

        //Creating Character as Key of storing Character of the string and value
        // as integer representing frequency of the character 
        HashMap<Character,Integer> map=new HashMap<Character,Integer>();

        //Checking length of both the strings and if not same returning false
        if(s.length() != t.length()){
            return false;
        }

        //Creating Character Array for both the strings
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        //Looping through the 1st String Array
        for(int i=0; i<sArr.length;i++){

            //Checking if hashmap contains the character, if yes increment its value by 1
            //else initializing the value to 1
            if(map.get(sArr[i]) != null){
                map.put(sArr[i],map.get(sArr[i])+1);
            }else{
                map.put(sArr[i],1);
            }
        }

        //Looping through the 2nd string
        for(int i=0; i<tArr.length;i++){

            //Checking if the character exists in map or its value is already zero
            // returning false if yes otherwise decrementing the value of the character by 1
            if(map.get(tArr[i]) == null || map.get(tArr[i]) == 0){
                return false;
            }else{
                map.put(tArr[i],map.get(tArr[i])-1);
            }
        }

        // Returning true atlast which means string are anagram
        return true;
    }
}


// Same Hashmap Solution as above but without converting string to array
// Saving space and faster in time
class Solution4b {
    public boolean isAnagram(String s, String t) {

        HashMap<Character,Integer> map=new HashMap<Character,Integer>();
        if(s.length() != t.length()){
            return false;
        }

        for(int i=0; i<s.length();i++){

            //Using charAt method to get the char by index while looping till the length \
            // of the string
            if(map.get(s.charAt(i)) != null){
                map.put(s.charAt(i),map.get(s.charAt(i))+1);
            }else{
                map.put(s.charAt(i),1);
            }
        }

        for(int i=0; i<t.length();i++){
            if(map.get(t.charAt(i)) == null || map.get(t.charAt(i)) == 0){
                return false;
            }else{
                map.put(t.charAt(i),map.get(t.charAt(i))-1);
            }
        }
        
        return true;
    }
}