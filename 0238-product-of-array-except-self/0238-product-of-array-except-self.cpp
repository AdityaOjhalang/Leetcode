class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n, 0);
        vector<int> suffix(n, 0);
        vector<int> result(n,0);
        prefix[0] = nums[0];
        for(int i=1;i<n;i++){
            prefix[i] = prefix[i - 1] * nums[i];
        }
        suffix[n-1] = nums[n-1];
        for(int i=n-2;i>=0;i--){
            suffix[i] = suffix[i + 1] * nums[i];
        }
        for(int i=0;i<n;i++){
            if(i==0){
                result[i] = suffix[i+1];
            }
            else if(i==n-1){
                result[i] = prefix[n-2];
            }
            else{
                result[i] = prefix[i-1]*suffix[i+1];
            }
        }
        return result;
    }
};