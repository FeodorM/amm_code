package main.ru.vsu.amm.problems

import main.ru.vsu.amm.problems.entities.{IntMatrix, Matrix}

/**
  * Created by FManukovskiy on 31.10.17.
  */
object Main {
  def main(args: Array[String]): Unit = {
//    val m = new Matrix(Seq(
//      Seq(1, 2, 3),
//      Seq(2, 4, 5),
//      Seq(2, 4, 5)
//    ))
    val m = IntMatrix.parse("input/matr")
    println(m)
    println()
    println(m.solved)
  }
}
