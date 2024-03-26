class Solution {
public:
    int longestAlternatingSubarray(std::vector<int>& nums, int threshold) {
        int maxLen = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] % 2 == 0 && nums[i] <= threshold) {
                int count = 1;
                for (int j = i; j < nums.size() - 1; j++) {
                    if (nums[j] % 2 != nums[j + 1] % 2 && nums[j + 1] <= threshold) {
                        count++;
                    } else {
                        break;
                    }
                }
                maxLen = std::max(maxLen, count);
            }
        }

        return maxLen;
    }
};