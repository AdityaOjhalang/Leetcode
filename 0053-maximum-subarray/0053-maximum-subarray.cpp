class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currmax = nums[0];
        int res = nums[0];
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            currmax = max(nums[i] + currmax, nums[i]);
            if (currmax > res) {
                res = currmax;
            }
        }

        return res;
    }
};