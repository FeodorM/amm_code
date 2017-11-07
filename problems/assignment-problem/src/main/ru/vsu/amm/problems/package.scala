package main.ru.vsu.amm

import main.ru.vsu.amm.problems.entities.{IntMatrix, Matrix, OrderedMatrix}

/**
  * Created by FManukovskiy on 31.10.17.
  */
package object problems {
  implicit def convert[B](data: Seq[Seq[B]]): Matrix[B] = new Matrix(data)

  implicit def convertToIntMatrix(data: Matrix[Int]): IntMatrix = new IntMatrix(data.data)
  implicit def convertFromIntMatrix(data: IntMatrix): Matrix[Int] = new Matrix[Int](data.data)

  implicit def convertToOrderedMatrix[T <: Ordered[T]](data: Matrix[T]): OrderedMatrix[T] = new OrderedMatrix[T](data.data)
  implicit def convertFromOrderedMatrix[T <: Ordered[T]](data: OrderedMatrix[T]): Matrix[T] = new Matrix[T](data.data)
}
