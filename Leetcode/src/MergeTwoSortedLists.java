public class MergeTwoSortedLists {
    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null)
            return l2;
        else if (l2 == null)
            return l1;

        if (l1.val < l2.val){
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        }
        else{
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }

    // Not well thought out...
    /*
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = l1.val > l2.val ? l1 : l2;
        ListNode temp = head;
        while (l1.next != null || l2.next != null){
            if (l1.val <= l2.val){
                temp.next = l1;
                temp = temp.next;
                temp.next = null;
                l1 = l1.next;
                continue;
            }
            else if (l1.val > l2.val){
                temp.next = l2;
                temp = temp.next;
                temp.next = null;
                l2 = l2.next;
            }
        }
        if (l1 != null){
            temp.next = l1;
        }
        else if (l2.next != null){
            temp.next = l2;
        }
        return head;
    }
    */

}
