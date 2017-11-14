package main.ru.vsu.amm.problems

import main.ru.vsu.amm.problems.entities.{IntMatrix, Matrix}

import io.StdIn.readLine
import java.io._

import ru.vsu.amm.problems.entities.AssignmentMatrix

/**
  * Created by FManukovskiy on 31.10.17.
  */
object Main {

  val message =
    """
      |Commands:
      |new -- generate new random matrix
      |read -- read edited matrix
      |bad -- solve by bad method
      |good -- solve by good method
      |end|quit|exit
    """.stripMargin

  object Commands {
    val New = "new"
    val Read = "read"
    val Print = "print"
    val Bad = "bad"
    val Good = "good"
    val End = "end"
    val Quit = "quit"
    val Exit = "exit"
  }


  def main(args: Array[String]): Unit = {
    var matrix: AssignmentMatrix = IntMatrix.parse("input/matr")
    var size = matrix.size

    println(message)
    while (true) {
      readLine(">>> ").split(" ").foreach {
        case Commands.New =>
          generateNewMatrix(size)
          matrix = IntMatrix.parse("input/matr")
          println(matrix)
        case Commands.Read =>
          matrix = IntMatrix.parse("input/matr")
          println(matrix)
        case Commands.Print =>
          println(matrix)
        case Commands.Bad =>
          println(matrix.solved)
          if (matrix.solved.data.map(_.sum) != Seq.fill(size)(1) || matrix.solved.data.indices.map(matrix.solved.col(_)).map(_.sum).toSeq != Seq.fill(size)(1)) {
            println("Something Wrong...")
            println(matrix.solved.data.map(_.sum))
            println(matrix.solved.data.indices.map(matrix.solved.col(_)).map(_.sum))
            println(Seq.fill(size)(1))
          }
        case Commands.Good =>
          println("Not implemented yet")
        case Commands.End => return
        case Commands.Quit => return
        case Commands.Exit => return
        case x if "^size=\\d+$".r.pattern.matcher(x).find() =>
          size = x.split("=")(1).toInt
          println(s"New size is $size")
        case _ =>
          println("Wrong command")
      }
    }
  }

  def generateNewMatrix(size: Int): Unit = {
    val pw = new PrintWriter(new File("input/matr"))
    pw.write(IntMatrix.random(size).toString)
    pw.close()
  }
}
