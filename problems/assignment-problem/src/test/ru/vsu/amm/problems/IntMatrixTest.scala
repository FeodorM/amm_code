package ru.vsu.amm.problems

import main.ru.vsu.amm.problems.entities.IntMatrix
import org.junit.Test
import ru.vsu.amm.problems.entities.AssignmentMatrix

/**
  * Created by FManukovskiy on 07.11.17.
  */
class IntMatrixTest {
  @Test
  @throws[Exception]
  def solved(): Unit = {
    val m: AssignmentMatrix = IntMatrix.parse("input/test")
    val e = IntMatrix.parse("input/etalon")

    assert(m.solved == e)
  }

  @Test
  def test(): Unit = {
//    println(Seq.fill(2)(1))
  }
}