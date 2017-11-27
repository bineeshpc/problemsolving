// http://www.spoj.com/problems/ACPC10A/

import java.util.*;
import java.lang.*;

class WhatsNext {
	public static void main (String[] args) throws java.lang.Exception {
        Scanner scanner = new Scanner(System.in);
        int a, b, c, cd1, cd2, cr1, cr2;
        while (scanner.hasNext()) {
            a = scanner.nextInt();
            b = scanner.nextInt();
            c = scanner.nextInt();
            if (a ==0 && b == 0 && c == 0) {
                break;
            }
            cd1 = b - a;
            cd2 = c - b;
            if (cd1 == cd2) {
                System.out.println("AP " + (c + cd1));
            }
            else {
                if (a != 0 && b != 0) {
                    cr1 = b / a;
                    cr2 = c / b;
                }
                else {
                    break;
                }
                if(cr1 == cr2){
                    System.out.println("GP " + (c * cr1));
                }
            }
        }

	}
}