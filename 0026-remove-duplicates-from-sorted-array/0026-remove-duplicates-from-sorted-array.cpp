class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int toadd = 1;
        for (int i=1;i<nums.size();i++){
            if(nums[i] != nums[i-1]){
                nums[toadd] = nums[i];
                toadd++;
            }
        }
        return toadd;
    }
};