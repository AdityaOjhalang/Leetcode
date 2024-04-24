class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t pos = haystack.find(needle);

        // If find returns std::string::npos, it means the substring was not
        // found.
        if (pos == string::npos) {
            return -1; // Return -1 if the substring is not found
        } else {
            return static_cast<int>(
                pos); // Cast size_t to int and return the position
        }
    }
};