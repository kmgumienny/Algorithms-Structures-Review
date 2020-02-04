public class AddTwoNums {

     //Definition for singly-linked list.
     public class ListNode {
         int val;
        ListNode next;
         ListNode(int x) { val = x; }
     }

    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            if (l1 == null) return l2;
            if (l2 == null) return l1;
            ListNode ans_head = new ListNode(0);
            ListNode curr = ans_head;
            int sum = 0;

            while (l1 != null || l2 != null){
                sum /= 10;
                if (l1 != null){
                    sum += l1.val;
                    l1 = l1.next;
                }
                if (l2 != null){
                    sum += l2.val;
                    l2 = l2.next;
                }
                curr.next = new ListNode(sum%10);
                curr = curr.next;
            }

            if (sum / 10 ==1)
                curr.next = new ListNode(1);

            return ans_head.next;


        }
    }
}
