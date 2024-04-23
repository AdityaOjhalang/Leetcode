class Solution {
public:
    string reverseWords(string s) {

        string temp = "";
        string ans = "";

        int n = s.size();
        bool first = true;

        for (int i = 0; i < n; i++) {
            if (s[i] != ' ') {
                temp += s[i];
            } else {
                if (temp.size() > 0) {
                    if (first) {
                        ans += temp;
                        first = false;
                    } else {
                        ans = (temp + " " + ans);
                    }
                }
                temp = "";
            }
        }

        if (temp.size() > 0) {
            if (first) {
                ans += temp;
                first = false;
            } else {
                ans = (temp + " " + ans);
            }
        }
        return ans;

    }
};