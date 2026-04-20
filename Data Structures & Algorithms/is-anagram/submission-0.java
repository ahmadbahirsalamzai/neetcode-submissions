class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        HashMap<Character, Integer> map = new HashMap<>();

        //each letter has to exist in each string the same # of times. 
        //add everything to the HashMap --> 1 loop
        for(char curr : s.toCharArray()){
            map.put(curr, map.getOrDefault(curr, 0) +1);
        }
        
        for(char curr : t.toCharArray()){
            map.put(curr, map.getOrDefault(curr,0) -1);
        }


        for(var curr : map.entrySet()){
            if(curr.getValue() != 0){
                return false;
            }
        }
        return true;
    }
}
