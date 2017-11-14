package main.ru.vsu.amm

import main.ru.vsu.amm.problems.entities.{IntMatrix, Matrix}
import ru.vsu.amm.problems.entities.{AssignmentMatrix, AssignmentMatrixBad, AssignmentMatrixGood}

/**
  * Created by FManukovskiy on 31.10.17.
  *
  * Some useful converters
  */
package object problems {
  /** Seq[Seq[T]] <--> Matrix[B] */
  implicit def convertSeqToMatrix[B](data: Seq[Seq[B]]): Matrix[B] = new Matrix(data)

  /** Matrix[B] <--> IntMatrix */
  implicit def convertToIntMatrix(data: Matrix[Int]): IntMatrix = new IntMatrix(data.data)

  implicit def convertFromIntMatrix(data: IntMatrix): Matrix[Int] = new Matrix[Int](data.data)

  /** Matrix[B] <--> AssignmentMatrix */
  implicit def convertFromAssignment(data: AssignmentMatrix): IntMatrix = new IntMatrix(data.data)

  implicit def convertToAssignment(data: IntMatrix): AssignmentMatrix = new AssignmentMatrix(data.data)

  /** AssignmentMatrix <--> AssignmentMatrixBad */
  implicit def convertFromAssignmentBad(data: AssignmentMatrixBad): AssignmentMatrix = new AssignmentMatrix(data.data)

  implicit def convertToAssignmentBad(data: AssignmentMatrix): AssignmentMatrixBad = new AssignmentMatrixBad(data.data)

  /** AssignmentMatrix <--> AssignmentMatrixGood */
  implicit def convertFromAssignmentGood(data: AssignmentMatrixGood): AssignmentMatrix = new AssignmentMatrix(data.data)

  implicit def convertToAssignmentGood(data: AssignmentMatrix): AssignmentMatrixGood = new AssignmentMatrixGood(data.data)
}
