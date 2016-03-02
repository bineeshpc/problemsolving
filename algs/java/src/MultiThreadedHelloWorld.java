public class MultiThreadedHelloWorld {
    
    public static void main(String[] args) throws InterruptedException {
    	Thread myThread = new Thread() {
    		public void run(){
			System.out.println("Hello World from Thread");
    		}
    	};
    	myThread.start();
    	Thread.yield();
    	//Thread.sleep(1);
    	System.out.println("Hello World from Main thread");
    	myThread.join();

    }
}