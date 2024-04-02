class Solution {
public:
    int hIndex(vector<int>& arr) {
        int n = arr.size();
        sort(arr.begin(), arr.end(),greater<int>());
        for(int i=0;i<n;i++){
            if(arr[i] <= i){
                return i;
            }
        }
    return n;
    }
};