#include "vector.h"

class TridiagonalMatrix
{
private:
	int size;
	Vector a;
	Vector b;
	Vector c;
	void AllocateMemory(int);
	void FreeMemory();
public:
	TridiagonalMatrix() : size(0), a(Vector()), b(Vector()), c(Vector()) {}	// Конструктор по умолчанию
	TridiagonalMatrix(const TridiagonalMatrix &);							// Конструктор копирования
	TridiagonalMatrix(int, Vector, Vector, Vector);							// Конструктор матрицы из трёх векторов
	~TridiagonalMatrix();													// Деструктор
	// предусмотреть конструктор создания матрицы, заполненной случайными числами
	// желательно предусмотреть конструктор (или метод), заполняющий матрицу из файла
	// во всех конструкторах предусмотреть, что a(0)=c(n-1)=0

	TridiagonalMatrix&operator=(const TridiagonalMatrix &);	// Перегрузка оператора присваивания
	TridiagonalMatrix operator+(const TridiagonalMatrix &);	// Сложение матриц
	TridiagonalMatrix operator-(const TridiagonalMatrix &);	// Вычитание матриц
	TridiagonalMatrix operator*(const TridiagonalMatrix &);	// Умножение матриц
	Vector operator*(const Vector &);	// Умножение матрицы на вектор

	// метод решения СЛАУ Ax=d может быть объявлен, например, следующим образом:
	// Vector linsolve(Vector &);
};

TridiagonalMatrix::TridiagonalMatrix(const TridiagonalMatrix &m)
{
}

TridiagonalMatrix::TridiagonalMatrix(int n, Vector A, Vector B, Vector C)
{
}

TridiagonalMatrix::~TridiagonalMatrix()
{
}

TridiagonalMatrix& TridiagonalMatrix::operator=(const TridiagonalMatrix &m)
{
	size = m.size;
	a = m.a;
	b = m.b;
	c = m.c;
	return *this;
}

TridiagonalMatrix TridiagonalMatrix::operator+(const TridiagonalMatrix &m)
{
	TridiagonalMatrix res(*this);
	if (size == m.size)
	{
		res.a = a + m.a;
		// ...
	}
	return res;
}

TridiagonalMatrix TridiagonalMatrix::operator-(const TridiagonalMatrix &m)
{
	// вычитание матриц
	return TridiagonalMatrix();
}

TridiagonalMatrix TridiagonalMatrix::operator*(const TridiagonalMatrix &m)
{
	// умножение матриц
	return TridiagonalMatrix();
}

Vector TridiagonalMatrix::operator*(const Vector &v)
{
	// умножение матриц
	return Vector();
}
