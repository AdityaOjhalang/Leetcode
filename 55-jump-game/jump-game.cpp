class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxreach = nums[0];
        int n = nums.size();
        if (n == 1) {
            return true;
        }
        for (int i = 0; i < n; i++) {

            maxreach = max(maxreach, nums[i] + i);

            if (maxreach <= i && nums[i] == 0) {
                return false;
            } else if (maxreach >= n - 1) {
                return true;
            }
        }

        return false;
    }
};