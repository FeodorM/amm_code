package main.ru.vsu.amm.problems.entities

import scala.collection.mutable
import main.ru.vsu.amm.problems._
import main.ru.vsu.amm.problems.exceptions.{AllDoneException, MatrixException}

/**
  * Created by FManukovskiy on 31.10.17.
  */
class Matrix[T](matrix: Seq[Seq[T]]) extends Serializable {
  val AllDone = new AllDoneException

  val data: Seq[Seq[T]] = matrix.map(_.map(x => x))
  if (data.exists(_.length != data.length)) {
    throw new MatrixException("Wrong size")
  }

//  def this(matrix: Matrix[T]) {
//    this(matrix.data)
//  }

  override def toString: String = data
    .map(_.mkString("\t"))
    .mkString("\n")


  def size: Int = data.size

  def iterator: Iterator[Seq[T]] = data.iterator

  def transpose: Matrix[T] = data.indices.map(col)

  def ==(matrix: Matrix[T]): Boolean = data.zip(matrix.data).forall({case (x, y) => x == y})


  def forall(func: (T) => Boolean): Boolean = data.forall(_.forall(func) == true)

  def exists(func: (T) => Boolean): Boolean = data.exists(_.exists(func))

  def map[B](func: (T) => B): Matrix[B] = data.map(_.map(func))

  def mapRows[B](func: (Seq[T]) => Seq[B]): Matrix[B] = data.map(func)

  def mapCols[B](func: (Seq[T]) => Seq[B])(implicit ev$1: B => T): Matrix[B] = data.indices.map(col).map(func).transpose[B]

  def mapRow(index: Int, func: (T) => T): Matrix[T] = data.updated(index, row(index).map(func))

  def mapCol(index: Int, func: (T) => T): Matrix[T] = data.transpose[T].updated(index, col(index).map(func)).transpose[T]


  def minBy[B](func: (T) => B)(implicit ev$1: B => Ordered[B]): T = data.map(_.minBy(func)).minBy(func)


  def row(n: Int): Seq[T] = data(n)

  def col(n: Int): Seq[T] = data.map(_(n))

  def rows: Seq[Seq[T]] = data

  def cols: Seq[Seq[T]] = data.indices.map(col)

}

object Matrix {
  def matrixOfIndices(size: Int): Matrix[(Int, Int)] =
    new Matrix[(Int, Int)]((0 until size).map(x => (0 until size).map(y => (x, y))))
}