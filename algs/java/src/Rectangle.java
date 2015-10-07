
public class Rectangle {
	Point p1, p2;
	public Rectangle(Point p1, Point p2) {
		this.p1 = p1;
		this.p2 = p2;
	}
	public double area() {
		// TODO Auto-generated method stub
		double xdiff, ydiff;
		xdiff = Math.abs(this.p1.x - this.p2.x);
		ydiff = Math.abs(this.p1.y - this.p2.y);
		return xdiff * ydiff;
	}

}
