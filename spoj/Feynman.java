// http://www.spoj.com/problems/SAMER08F/

import java.util.*;
import java.lang.*;


class Feynman {
        public static void main (String[] args) throws java.lang.Exception {
        Scanner scanner = new Scanner(System.in);
        int n;
        while (scanner.hasNext()) {
            n = scanner.nextInt();
            if (n == 0)
                break;
            else {
                System.out.println(n * (n + 1) * (2 * n + 1) / 6);
            }
        }
    }
}