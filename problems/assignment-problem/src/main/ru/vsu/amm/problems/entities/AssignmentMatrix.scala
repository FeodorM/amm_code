package ru.vsu.amm.problems.entities

import main.ru.vsu.amm.problems.entities.IntMatrix

/**
  * Created by FManukovskiy on 14.11.17.
  */
class AssignmentMatrix(matrix: Seq[Seq[Int]]) extends IntMatrix(matrix) {

  lazy val isReduced: Boolean = forall(_ >= 0) && cols.forall(_.exists(_ == 0)) && rows.forall(_.exists(_ == 0))

  lazy val reduced: IntMatrix = {
    if (isReduced) {
      this
    } else {
      val reducedByRows: AssignmentMatrix = mapRows(row => row.map(_ - row.min)).toInt

      if (reducedByRows.isReduced) {
        reducedByRows
      } else {
        reducedByRows.mapCols(col => col.map(_ - col.min))
      }
    }
  }

  def toAssignment: AssignmentMatrix = this
}
