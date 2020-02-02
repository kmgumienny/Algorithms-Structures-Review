public class LengthLastWord {

    public int LengthLastWord(String s) {
        if (s.length() == 0)
            return 0;
        int curr_length = 0;
        int last_length = 0;

        char[] as_chars = s.toCharArray();

        for (int i = 0; i < as_chars.length; i++) {
            if (as_chars[i] != ' ') {
                curr_length += 1;
            } else if (curr_length > 0) {
                last_length = curr_length;
                curr_length = 0;
            }
        }

        if (curr_length == 0)
            return last_length;

        return curr_length;
    }
}
