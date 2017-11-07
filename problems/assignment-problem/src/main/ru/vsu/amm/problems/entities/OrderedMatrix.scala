package main.ru.vsu.amm.problems.entities

/**
  * Created by FManukovskiy on 31.10.17.
  */
class OrderedMatrix[T <: Ordered[T]](matrix: Seq[Seq[T]]) extends Matrix[T](matrix) {
  def min: T = data.map(_.min).min
}
