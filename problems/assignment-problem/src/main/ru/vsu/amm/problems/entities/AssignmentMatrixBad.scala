package ru.vsu.amm.problems.entities

import main.ru.vsu.amm.problems.entities.{IntMatrix, Matrix}

import scala.collection.mutable
import scala.util.Try

/**
  * Created by FManukovskiy on 14.11.17.
  */
class AssignmentMatrixBad(matrix: Seq[Seq[Int]]) extends AssignmentMatrix(matrix) {
  protected def crossRows(matrix: Matrix[(Int, Int)], numberOfCrossings: Int): Matrix[(Int, Int)] = {
    //    println("row") //todo
    val rowIndex = matrix.data
      .indices
      .find(matrix.row(_).count(_ == (0, 0)) == numberOfCrossings)
      .get
    //    println(rowIndex)

    val indices = matrix.data
      .indices
      .filter(i => matrix.row(rowIndex).slice(i, matrix.size).indexOf((0, 0)) == 0)

    //    matrix.data
    //      .indices
    //      .foreach(i => println(matrix.row(rowIndex).slice(i, matrix.size).indexOf((0, 0))))
    //    println(indices)

    var resultMatrix = matrix
    for (ind <- indices) {
      resultMatrix = resultMatrix
        .mapCol(ind, { case (x: Int, y: Int) => (x, y + 1) })
    }
    //    println(resultMatrix)
    resultMatrix
  }

  protected def crossColumns(matrix: Matrix[(Int, Int)], numberOfCrossings: Int): Matrix[(Int, Int)] = {
    //    println("col") //todo
    val colIndex = matrix.data
      .indices
      .find(matrix.col(_).count(_ == (0, 0)) == numberOfCrossings)
      .get

    val indices = matrix.data
      .indices
      .filter(i => matrix.col(colIndex).slice(i, matrix.size).indexOf((0, 0)) == 0)

    var resultMatrix = matrix
    for (ind <- indices) {
      resultMatrix = resultMatrix
        .mapRow(ind, { case (x: Int, y: Int) => (x, y + 1) })
    }
    resultMatrix
  }

  protected lazy val crossAndCountIndependentZeros: (Matrix[(Int, Int)], Int) = {
    var matrix = reduced.map((_, 0))
    var count = 0

    var continueFor = true
    var continueWhile = true

    while (count != matrix.size && continueWhile) {
      continueFor = true
      for (numberOfCrossings <- 1 to matrix.size if continueFor) {
        //        println(matrix) // todo
        //        println(s"$numberOfCrossings -- $count")
        val a = Try(crossRows(matrix, numberOfCrossings))
        if (a.isSuccess) {
          matrix = a.get
          count += numberOfCrossings
          continueFor = false
        } else {
          val a = Try(crossColumns(matrix, numberOfCrossings))
          if (a.isSuccess) {
            matrix = a.get
            count += numberOfCrossings
            continueFor = false
          } else {
            continueFor = true
          }
        }
        if (numberOfCrossings == matrix.size) {
          continueWhile = false
        }
      }
    }
    (matrix, count)
  }

  lazy val crossed: Matrix[(Int, Int)] = crossAndCountIndependentZeros._1

  lazy val independentZerosNumber: Int = crossAndCountIndependentZeros._2



  protected def crossRowsWithIndices(matrix: Matrix[(Int, Int)], numberOfCrossings: Int): (Matrix[(Int, Int)], (Int, Int)) = {
    //    println("row") //todo
    val rowIndex = matrix.data
      .indices
      .find(matrix.row(_).count(_ == (0, 0)) == numberOfCrossings)
      .get

    val colIndex = matrix.data
      .indices
      .find(i => matrix.row(rowIndex).slice(i, matrix.size).indexOf((0, 0)) == 0)
      .get

    (matrix
      .mapCol(colIndex, { case (x: Int, y: Int) => (x, y + 1) })
      .mapRow(rowIndex, { case (x: Int, y: Int) => (x, y + 1) }),
      (rowIndex, colIndex))
  }

  protected def crossColumnsWithIndices(matrix: Matrix[(Int, Int)], numberOfCrossings: Int): (Matrix[(Int, Int)], (Int, Int)) = {
    //    println("col") //todo
    val colIndex = matrix.data
      .indices
      .find(matrix.col(_).count(_ == (0, 0)) == numberOfCrossings)
      .get

    val rowIndex = matrix.data
      .indices
      .find(i => matrix.col(colIndex).slice(i, matrix.size).indexOf((0, 0)) == 0)
      .get

    (matrix
      .mapCol(colIndex, { case (x: Int, y: Int) => (x, y + 1) })
      .mapRow(rowIndex, { case (x: Int, y: Int) => (x, y + 1) }),
      (rowIndex, colIndex))
  }

  protected lazy val independentZerosIndices: Seq[(Int, Int)] = {
    var matrix = reduced.map((_, 0))
    val zerosIndices = new mutable.ListBuffer[(Int, Int)]()
    var count = 0

    var continueFor = true
    var continueWhile = true

    while (count != matrix.size && continueWhile) {
      continueFor = true
      for (numberOfCrossings <- 1 to matrix.size if continueFor) {
        //                println(matrix) // todo
        //                println(s"$numberOfCrossings -- $count")
        val a = Try(crossRowsWithIndices(matrix, numberOfCrossings))
        if (a.isSuccess) {
          a.get match {
            case (m, indices) =>
              matrix = m
              zerosIndices.append(indices)
          }
          count += 1
          continueFor = false
        } else {
          val a = Try(crossColumnsWithIndices(matrix, numberOfCrossings))
          if (a.isSuccess) {
            a.get match {
              case (m, indices) =>
                matrix = m
                zerosIndices.append(indices)
            }
            count += 1
            continueFor = false
          } else {
            continueFor = true
          }
        }
        if (numberOfCrossings == matrix.size) {
          continueWhile = false
        }
      }
    }
    zerosIndices
  }

  lazy val withNewZeros: IntMatrix = {
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

  lazy val solvedIndices: Seq[(Int, Int)] = {
    var m: AssignmentMatrix = this.reduced

    while (m.independentZerosNumber != m.size && m != m.withNewZeros) {
      m = m.withNewZeros
      //      println(s"${m.independentZerosNumber}-${m.size}")
      //      println(m)
      //      println()
    }
    m.independentZerosIndices
  }

  lazy val solved: IntMatrix = Matrix.matrixOfIndices(size)
    .map(ind => if (solvedIndices.contains(ind)) 1 else 0)
}
