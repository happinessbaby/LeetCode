
object Solution {
    def runningSum(nums: Array[Int]): Array[Int] = {
        //var res: Array[Int] = Array[Int](nums.size)
        //var x = 0
        // nums.foreach{num=>
        //     x += num
        //     res :+ x
        // }
        // var res = nums.map{
        //     var x = 0;
        //     d=>{x+=d; x}
        // }
        // res
        val res = nums.scanLeft(0)(_+_)
        res.drop(1)
    }
}