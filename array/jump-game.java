class Solution {
    public boolean canJump(int[] nums) {
      int rightPos = 0;
      int n = nums.length;
      int cur = 0;
      while(cur<=rightPos){
        int pos = cur+nums[cur];
        rightPos = Math.max(rightPos, pos);
        cur++;
      }
      return rightPos >= n-1;
    }
}