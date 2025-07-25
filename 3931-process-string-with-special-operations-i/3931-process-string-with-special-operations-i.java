class Solution {
    public String processStr(String s) {
        StringBuilder sb = new StringBuilder();
    for(int i =0; i<s.length(); i++){
        char ch = s.charAt(i);
        if(Character.isLetter(ch)){
            sb.append(ch);
        }
        else if(ch=='*'){
            if(sb.length()>0){
                sb.deleteCharAt(sb.length()-1);
            }
        }
        else if(ch=='#'){
            String dup = sb.toString();
            sb.append(dup);
        }
        else if(ch == '%'){
            sb.reverse();
        }
    }
    return sb.toString();
    }
}