class Solution {
    public int[] twoSum(int[] nums, int target) {
       Map<Integer, Integer> my_map = new HashMap<>();
       for(int i = 0; i < nums.length; i++){
            int comp = target - nums[i];
            if (my_map.containsKey(comp)){
                return new int[] {my_map.get(comp), i};
            }
            my_map.put(nums[i], i);
       }
       return null;
    }
}
