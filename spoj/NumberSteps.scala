// http://www.spoj.com/problems/NSTEPS/


object NumberSteps {
	// your code goes here

    def in_line(x:Int, y: Int) : Boolean = {
        return (x == y + 2) || (x == y)
    }

    def get_num_in_position(x: Int, y: Int) : Int = {
        if (x % 2 == 0) {
            return x + y
        } 
        else {
            return x + y - 1
        }
    }
    def main(args: Array[String]) {
      val num_cases : Int = scala.io.StdIn.readInt()
      var count: Int = 0
      while(count < num_cases) {
        var str: String = scala.io.StdIn.readLine()
        var str_array: Array[String] = new Array[String](2)
        str_array = str.split(" ")
        var x: Int = str_array(0).toInt
        var y: Int = str_array(1).toInt
        if (in_line(x, y))
            println(get_num_in_position(x, y))
        else
            println("No Number")
        count += 1
      }
   }
}