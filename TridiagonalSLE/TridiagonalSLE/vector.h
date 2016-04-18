#include <iostream>

using namespace std;

typedef double Cell;		// ��� ��������� �������

class Vector
{
private:
	int size;		// ������ �������
	Cell *cell;		// �������� �������
	void AllocateMemory(int);
	void FreeMemory();
public:
	Vector() : size(0), cell(NULL) {}	// ����������� �� ���������
	Vector(const Vector &);				// ����������� �����������
	Vector(int, Cell*);					// ����������� ������� �� ������ Cell
	~Vector();							// ����������
	// ������������� ����������� �������� �������, ������������ ���������� �������
	// ������������� ����������� (��� �����), ����������� ������ �� �����; ��� ����� ��������� � �������� ���������

	Cell &operator()(int i) { return cell[i]; }
	
	Vector&operator=(const Vector &);	// ���������� ��������� ������������
	Vector operator+(const Vector &);	// �������� ��������
	Vector operator-(const Vector &);	// ��������� ��������
	Cell operator*(const Vector &);		// ��������� ��������� ��������
	// �������� ����� - ���������� ����� �������

	friend istream &operator>>(istream &, Vector &);		// ���������� ��������� >> ��� ����� �������
	friend ostream &operator<<(ostream &, const Vector &);	// ���������� ��������� << ��� ������ �������
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
//		���������� ������� ���������� �� ������ list
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
	// ��������� ��������
}

Cell Vector::operator*(const Vector &v)
{
	// ��������� ��������� ��������
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
