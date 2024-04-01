class Solution {
public:
    int jump(vector<int>& nums) {
        int minJumps = 0;
        int currentEnd = 0;
        int farthest = 0;

        // We don't need to check the last element because we are already
        // jumping to it.
        for (int i = 0; i < nums.size() - 1; i++) {
            farthest = max(farthest, i + nums[i]);

            // We are allowed to jump and we have reached the end of our current
            // jump, so we have to make another jump.
            if (i == currentEnd) {
                minJumps++;
                currentEnd = farthest;

                // If our current jump can reach the end, we break the loop.
                if (currentEnd >= nums.size() - 1) {
                    break;
                }
            }
        }

        return minJumps;
    }
};