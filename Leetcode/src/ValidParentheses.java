public class PalindromeNumber{

//     public static void main(String[] args){
//         boolean answer = isPalindrome(121);
//     }

    public boolean isValid(String s) {
        if (s.length() == 0)
            return true;
        if (s.length() % 2 == 1)
            return false;

        int len = s.length();

        Map<Character, Character> parens = new HashMap<>();
        parens.put(']', '[');
        parens.put('}', '{');
        parens.put(')', '(');

        Stack<Character> aStack = new Stack();

        for(int i = 0; i < s.length(); i++){
            char currChar = s.charAt(i);
            if (!aStack.empty() && parens.get(currChar) == aStack.peek())
                aStack.pop();
            else
                aStack.push(currChar);
        }
        return aStack.empty();

    }

// Took the wrong approach here. Should have used a stack instead...

/*
    public boolean isValid(String s) {
        if (s.length() == 0)
            return true;
        if (s.length() % 2 == 1)
            return false;

        int len = s.length();

        Map<Character, Character> parens = new HashMap<>();
        parens.put('[', ']');
        parens.put('{', '}');
        parens.put('(', ')');

        StringBuilder strbdr = new StringBuilder(s);

        while(strbdr.length() >= 2){

            if (parens.get(strbdr.charAt(0)) == null)
                return false;
            else if (parens.get(strbdr.charAt(0)) == strbdr.charAt(1)){
                strbdr = strbdr.deleteCharAt(0);
                strbdr = strbdr.deleteCharAt(0);
                continue;
            }
            else if ((parens.get(strbdr.charAt(0)) == strbdr.charAt(strbdr.length() - 1))){
                strbdr = strbdr.deleteCharAt(0);
                strbdr = strbdr.deleteCharAt(strbdr.length()-1);
                continue;
            }

            return false;

        }
        return true;

    }
*/
}