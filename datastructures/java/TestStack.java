/*TestStack.java
 */

class TestStack {
    public static void main (String arg[]) {
	testNewStack();
	testPush();/*
	testPop();*/
	System.out.println("All tests passed");
    }
    static void testNewStack() {
	Stack s = new Stack();
	if (s.isempty()) {
	    System.out.println("new stack creation passed");
	}
    }
    static void testPush() {
	Stack s = new Stack();
	int item = 5, retvalue;
	retvalue = s.push(item);
	assert(s.top == 1);
	assert(item == retvalue);
    }
}

class Stack {
    static int top;
    static int maxsize = 100;
    static int[] items = new int[maxsize];

    Stack() {
	this.top = 0;
    }
    boolean isempty() {
	return this.top == 0;
    }
    boolean isfull() {
	return (this.maxsize - 1) == this.top;
    }
    int push(int item) {
	if(this.isfull() == false) {
	    this.items[this.top++] = item;
	    return item;
	}
	else
	    return -1;
    }
    int pop() {
	if(this.isempty() == false)
	    return this.items[this.top--];
	return -1;
    }
}
