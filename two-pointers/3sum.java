class Solution {
    public ArrayList<int[]> threeSum(int[] nums) {
    ArrayList<int[]> outputs = new ArrayList<int[]>();
    for(int i = 0; i < nums.length-2; i+=1) {
        for (int j = i +1; j <nums.length - 1; j+=1) {
          for (int k = i +1; j <nums.length -2; k+=1) {
            Boolean isvalid = false;
            if (nums[i]!=j & nums[i]!= k & nums[j]!=k) {
              if (nums[i] + nums[j] + nums[k] == 0) {
                isvalid= true;
                if (isvalid) {
                int valiseq[];
                int[] validseq = null;
				        validseq[0] = i;
                validseq[1] = j;
                validseq[2] = k;
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