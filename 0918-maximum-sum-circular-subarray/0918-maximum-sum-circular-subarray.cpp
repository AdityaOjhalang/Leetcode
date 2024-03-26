class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n = nums.size();
        int normal = maxSubArray(nums);
        int res = nums[0];
        int currmin = nums[0];
        for (int i = 1; i < n; i++) {
            currmin = min(nums[i] + currmin, nums[i]);
            res = min(res, currmin);
        }
        int total = 0;
        for (int i = 0; i < n; i++) {
            total += nums[i];
        }
        int circ = total - res;
        if (circ == 0)
            return normal;
        int ans = max(normal, circ);

        return ans;
    }
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