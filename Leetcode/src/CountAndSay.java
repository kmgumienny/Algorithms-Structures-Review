public class CountAndSay {

    class Solution {
        public String countAndSay(int n) {
            if (n == 1)
                return "1";
            else if (n ==2)
                return "11";

            StringBuilder answer = new StringBuilder();
            StringBuilder curr_run = new StringBuilder("11");
            StringBuilder ptr = new StringBuilder();

            for (int i = 2; i < n; i++){
                int run = 1;
                char curr_char = ' ';
                for (int j = 1; j < curr_run.length(); j++){
                    curr_char = curr_run.charAt(j-1);
                    if (curr_char == curr_run.charAt(j)){
                        run += 1;
                    }else{
                        answer.append(run);
                        answer.append(curr_char);
                        run = 1;
                    }
                }
                answer.append(run);
                answer.append(curr_run.charAt(curr_run.length() - 1));

                ptr = curr_run;
                curr_run = answer;
                answer = ptr;
                answer.delete(0, answer.length());
            }
            return curr_run.toString();
        }
    }


    // Not well thought out...
    /*
    public String countAndSay(int n) {
        StringBuilder answer = new StringBuilder();
        StringBuilder curr_run = new StringBuilder();
        StringBuilder ptr = new StringBuilder();

        curr_run.append('1');
        for (int i = 1; i < n; i++){
            int run = 1;
            char curr_char = ' ';
            char prev_char = ' ';
            for (int j = 0; j < curr_run.length(); j++){
                curr_char = curr_run.charAt(j);
                if (prev_char != curr_char || j == curr_run.length() - 1){
                    answer.insert(answer.length(), curr_char);
                    answer.insert(answer.length(), run);
                    run = 1;
                    prev_char = curr_char;
                }else if (curr_char == prev_char)
                    run++;
            }
            ptr = curr_run;
            curr_run = answer;
            answer = ptr;
            answer.delete(0, answer.length());
        }
        return curr_run.toString();
    }
     */
}
