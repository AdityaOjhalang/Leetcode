class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int threshold = n-1;
        // if(n==1 && nums[0] > 0){
        //     return true;
        // }
        for(int i=n-2;i>=0;i--){
            if(nums[i]+ i >= threshold){
                threshold =i;
            }
        }
        return threshold==0;
    }
};