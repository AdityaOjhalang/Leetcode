class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxdiff=0;
        int minval = prices[0];
        for(int i=0;i<prices.size();i++){
            maxdiff= max(maxdiff,prices[i]-minval);
            minval = min(prices[i],minval);
        }
        return maxdiff;
    }
};