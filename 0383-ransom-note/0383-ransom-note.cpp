class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map <char,int> map;

        for(int i=0;i<magazine.size();i++){
            map[magazine[i]] += 1;
        }


        for(int i=0;i<ransomNote.size();i++){
            char curr = ransomNote[i];

            if(map[curr]>0){
                map[curr] -= 1;

            }
            else{
                return false;
            }
        }

        return true;

    }
};