class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> my_map = new HashMap<>();

        // add all chars from s to the map with their count
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (my_map.containsKey(c)) {
                my_map.put(c, my_map.get(c) + 1);
            } else {
                my_map.put(c, 1);
            }
        }

        // compare the values from my_map to t
        HashMap<Character, Integer> map = new HashMap<>();
        for (int j = 0; j < t.length(); j++) {
            char ch = t.charAt(j);

            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
            }
        }

        return my_map.equals(map);
    }
}
