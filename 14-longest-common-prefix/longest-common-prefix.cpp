class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty())
            return " ";

        string prefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            int min_length = min(prefix.length(), strs[i].length());

            int j=0;
            while(j<min_length && prefix[j] == strs[i][j]){
                j++;
            }

            prefix.resize(j);

            if(prefix.empty())break;
        }
        return prefix;
    }
};