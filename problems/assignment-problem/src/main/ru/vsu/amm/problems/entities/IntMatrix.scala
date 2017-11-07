package main.ru.vsu.amm.problems.entities

import main.ru.vsu.amm.problems._

import scala.collection.mutable
import scala.io.Source

/**
  * Created by FManukovskiy on 31.10.17.
  */
class IntMatrix(matrix: Seq[Seq[Int]]) extends Matrix[Int](matrix) {

  def sum: Int = data.map(_.sum).sum

  def isReduced: Boolean = forall(_ >= 0) && cols.forall(_.exists(_ == 0)) && rows.forall(_.exists(_ == 0))

  def reduced: IntMatrix = {
    if (isReduced)
      return this

    val reducedByRows = mapRows(row => row.map(_ - row.min))

    if (reducedByRows.isReduced)
      return reducedByRows

    reducedByRows.mapCols(col => col.map(_ - col.min))
  }

  protected def independentZeros: (Matrix[(Int, Int)], Seq[(Int, Int)], Int) = {
    var matrix = reduced.map((_, 0))
    var zeros = new mutable.ListBuffer[(Int, Int)]()
    var count = 0

    try {
      while (true) {
        val rowInd = matrix.data
          .indices
          .filter(matrix.row(_).count(_ == (0, 0)) == 1)
          .head

        val ind = matrix.row(rowInd).indexOf((0, 0))
        matrix = matrix
          .mapCol(ind, { case (x: Int, y: Int) => (x, y + 1) })
        zeros += ((rowInd, ind))
        count += 1
      }
    } catch {
      case _: UnsupportedOperationException =>
      case _: NoSuchElementException =>
    }

    try {
      while (true) {
        val colInd = matrix.data
          .indices
          .filter(matrix.col(_).count(_ == (0, 0)) == 1)
          .head

        val ind = matrix.col(colInd).indexOf((0, 0))
        matrix = matrix
          .mapRow(ind, { case (x: Int, y: Int) => (x, y + 1) })
        zeros += ((ind, colInd))
        count += 1
      }
    } catch {
      case _: UnsupportedOperationException =>
      case _: NoSuchElementException =>
    }

    (matrix, zeros, count)
  }

  def crossed: Matrix[(Int, Int)] = independentZeros._1

  def independentZerosIndices: Seq[(Int, Int)] = independentZeros._2

  def independentZerosNumber: Int = independentZeros._3

  def withNewZeros: IntMatrix = {
    val min = crossed.minBy({
      case (x, 0) => x
      case (_, _) => Int.MaxValue
    })._1
    crossed.map({
      case (value, count) if count == 0 =>
        value - min
      case (value, count) if count == 1 =>
        value
      case (value, count) if count == 2 =>
        value + min
    })
  }

  def solvedIndices: Seq[(Int, Int)] = {
    var m = this.reduced
    while (m.independentZerosNumber != m.size) {
      m = m.withNewZeros
    }
    m.independentZerosIndices
  }

  def solved: IntMatrix = Matrix.matrixOfIndices(size)
    .map(ind =>
      if (solvedIndices.contains(ind))
        1
      else
        0
    )

}

object IntMatrix {
  def parse(filename: String): Matrix[Int] =
    Source.fromFile(filename)
      .getLines
      .map(line =>
        line.trim
          .split(" ")
          .map(_.toInt)
          .toSeq
      )
      .toSeq
}