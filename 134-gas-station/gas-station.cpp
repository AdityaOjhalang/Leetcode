class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        int n = gas.size();
        vector<int> diff(n);
        int gasSum = accumulate(gas.begin(), gas.end(), 0);
        int costSum = accumulate(cost.begin(), cost.end(), 0);

        int total = 0;
        int start = 0;

        if (gasSum < costSum) {
            return -1;
        } else {
            for (int i = 0; i < n; i++) {
                diff[i] = gas[i] - cost[i];
            }

            for (int i = 0; i < n; i++) {
                total += diff[i];
                if (total < 0) {
                    total = 0;
                    start = i + 1;
                }
            }
        }
        return start;
    }
};