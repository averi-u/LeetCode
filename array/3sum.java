class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> outputs = null;
    for(int i = 0; i < nums.length-2; i+=1) {
        for (int j = i +1; j <nums.length - 1; j+=1) {
          for (int k = i +1; j <nums.length -2; k+=1) {
            Boolean isvalid = false;
            if (nums[i]!=nums[j] & nums[i]!= nums[k] & nums[j]!=nums[k]) {
              if (nums[i] + nums[j] + nums[k] == 0) {
                isvalid= true;
                if (isvalid) {
                List<Integer> validseq = null;
				        validseq.add(i);
                validseq.add(j);
                validseq.add(k);
                outputs.add(validseq);
                }
                
              }
            }
          }
        }
    }
    return outputs;
    }
}