public class LongestCommonPrefix {
    public class longestCommonPrefix{

//    public static void main(String[] args){
//        String[] strings = {"Fish", "Filling", "Finish"};
//        String answer = longestCommonPrefix(strings);
//    }


        public String longestCommonPrefix(String[] strs) {
            StringBuilder answer = new StringBuilder("");
            if(strs.length == 0)
                return answer.toString();
            if(strs.length == 1)
                return strs[0];
            char[] first_string = strs[0].toCharArray();
            int size_first_string = first_string.length;
            int current_max_length = size_first_string < strs[1].length() ? size_first_string : strs[1].length();

            for (int i = 1; i < strs.length; i++){
                char[] next_string = strs[i].toCharArray();
                current_max_length = current_max_length <= next_string.length ? current_max_length : next_string.length;
                for (int j = 0; j < current_max_length; j++){
                    if (first_string[j] == next_string[j])
                        continue;
                    else if(j == 0)
                        return "";
                    else if(j >= 1)
                        current_max_length = j++;
                }
            }
            return answer.append(strs[0].substring(0, current_max_length)).toString();
        }
    }
}
