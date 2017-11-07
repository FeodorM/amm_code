package ru.vsu.amm.problems

import main.ru.vsu.amm.problems.entities.IntMatrix
import org.junit.Test

/**
  * Created by FManukovskiy on 07.11.17.
  */
class IntMatrixTest {
  @Test
  @throws[Exception]
  def solved(): Unit = {
    val m = IntMatrix.parse("input/matr")
    val e = IntMatrix.parse("input/etalon")

    assert(m.solved == e)
  }
}