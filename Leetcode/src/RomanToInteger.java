public class RomanToInteger{

//    public static void main(String[]args){
//        int answer = romanToInt("IV");
//        System.out.println(answer);
//    }


    public static int romanToInt(String s){
        int answer=0;
        char prev_char='S',curr_char;
        char[]chararray=s.toCharArray();
        for(int i=0;i<chararray.length;i++){
            switch(chararray[i]){
                case'M':
                answer+=1000;
                if(prev_char=='C')
                    answer-=200;
                prev_char='M';
                break;

                case'D':
                answer+=500;
                if(prev_char=='C')
                    answer-=200;
                prev_char='D';
                break;

                case'C':
                answer+=100;
                if(prev_char=='X')
                    answer-=20;
                prev_char='C';
                break;

                case'L':
                answer+=50;
                if(prev_char=='X')
                    answer-=20;
                prev_char='L';
                break;

                case'X':
                answer+=10;
                if(prev_char=='I')
                    answer-=2;
                prev_char='X';
                break;

                case'V':
                answer+=5;
                if(prev_char=='I')
                    answer-=2;
                prev_char='V';
                break;

                case'I':
                answer+=1;
                prev_char='I';
                break;
            }
        }

        return answer;
    }
}