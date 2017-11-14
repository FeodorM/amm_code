package main.ru.vsu.amm.problems.entities

import main.ru.vsu.amm.problems._

import scala.io.Source
import scala.util.Random

/**
  * Created by FManukovskiy on 31.10.17.
  */
class IntMatrix(matrix: Seq[Seq[Int]]) extends Matrix[Int](matrix) {

  lazy val sum: Int = data.map(_.sum).sum

  def toInt: IntMatrix = this
}

object IntMatrix {
  def parse(filename: String): IntMatrix =
    new Matrix[Int](Source.fromFile(filename)
      .getLines
      .map(line =>
        line.trim
          .split("\t")
          .flatMap(_.split(" "))
          .map(_.toInt)
          .toSeq
      )
      .toSeq)

  def random(size: Int): Matrix[Int] =
    Seq.fill(size)(Seq.fill(size)(Random.nextInt(10)))
}