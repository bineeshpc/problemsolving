
public class testRectangle {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Testing area of a unit rectangle");
		Rectangle r = new Rectangle(new Point(0., 0.), new Point(1., 1.));
		assert r.area() == 1;
		System.out.println("Testing area of a rectangle of area 2.0");
		Rectangle r2 = new Rectangle(new Point(0., 0.), new Point(2., 1.));
		System.out.println("area is " + r2.area());
		assert r2.area() == 2;
	}

}
