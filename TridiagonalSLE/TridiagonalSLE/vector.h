#include <iostream>

using namespace std;

typedef double Cell;		// тип элементов вектора

class Vector
{
private:
	int size;		// размер вектора
	Cell *cell;		// элементы вектора
	void AllocateMemory(int);
	void FreeMemory();
public:
	Vector() : size(0), cell(NULL) {}	// Конструктор по умолчанию
	Vector(const Vector &);				// Конструктор копирования
	Vector(int, Cell*);					// Конструктор матрицы из списка Cell
	~Vector();							// Деструктор
	// предусмотреть конструктор создания вектора, заполненного случайными числами
	// предусмотреть конструктор (или метод), заполняющий вектор из файла; имя файла передаётся в качестве параметра

	Cell &operator()(int i) { return cell[i]; }
	
	Vector&operator=(const Vector &);	// Перегрузка оператора присваивания
	Vector operator+(const Vector &);	// Сложение векторов
	Vector operator-(const Vector &);	// Вычитание векторов
	Cell operator*(const Vector &);		// Скалярное умножение векторов
	// добавить метод - вычисление нормы вектора

	friend istream &operator>>(istream &, Vector &);		// Перегрузка оператора >> для ввода матрицы
	friend ostream &operator<<(ostream &, const Vector &);	// Перегрузка оператора << для вывода матрицы
};

Vector::Vector(const Vector &v)
{
	AllocateMemory(v.size);
	for (int i=0; i<size; i++)
		cell[i] = v.cell[i];
}

Vector::Vector(int n, Cell* list=NULL)
{
	AllocateMemory(n);
	if (list==NULL)
		for (int i=0; i<size; i++)
			cell[i] = 0;
	else
//		заполнение матрицы элементами из списка list
		for (int i=0; i<size; i++)
			cell[i] = list[i];
}

Vector::~Vector()
{
	FreeMemory();
}

Vector& Vector::operator=(const Vector &v)
{
	if (size != v.size)
	{
		FreeMemory();
		AllocateMemory(v.size);
	}
	for (int i=0; i<size; i++)
		cell[i] = v.cell[i];
	return *this;
}

Vector Vector::operator+(const Vector &v)
{
	Vector res(*this);
	if (size == v.size)
	{
		for (int i=0; i<size; i++)
			res.cell[i]+=v.cell[i];
	}
	return res;
}

Vector Vector::operator-(const Vector &v)
{
	// вычитание векторов
}

Cell Vector::operator*(const Vector &v)
{
	// скалярное умножение векторов
}

istream &operator>>(istream &fi, Vector &v)
{
	for (int i=0; i<v.size; i++)
		fi >> v.cell[i];
	return fi;
}

ostream &operator<<(ostream &fo, const Vector &v)
{
	for (int i=0; i<v.size; i++)
	{
		fo << v.cell[i] << " \t";
	}
	fo << "\n";
	return fo;
}

void Vector::AllocateMemory(int n)
{
	size=n;
	cell = new Cell[size];
}

void Vector::FreeMemory()
{
	delete cell;
	size=0;
}
