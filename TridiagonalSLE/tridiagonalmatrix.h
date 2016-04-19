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
	TridiagonalMatrix() : size(0), a(Vector()), b(Vector()), c(Vector()) {}	// ����������� �� ���������
	TridiagonalMatrix(const TridiagonalMatrix &);							// ����������� �����������
	TridiagonalMatrix(int, Vector, Vector, Vector);							// ����������� ������� �� ��� ��������
	~TridiagonalMatrix();													// ����������
	// ������������� ����������� �������� �������, ����������� ���������� �������
	// ���������� ������������� ����������� (��� �����), ����������� ������� �� �����
	// �� ���� ������������� �������������, ��� a(0)=c(n-1)=0

	TridiagonalMatrix&operator=(const TridiagonalMatrix &);	// ���������� ��������� ������������
	TridiagonalMatrix operator+(const TridiagonalMatrix &);	// �������� ������
	TridiagonalMatrix operator-(const TridiagonalMatrix &);	// ��������� ������
	TridiagonalMatrix operator*(const TridiagonalMatrix &);	// ��������� ������
	Vector operator*(const Vector &);	// ��������� ������� �� ������

	// ����� ������� ���� Ax=d ����� ���� ��������, ��������, ��������� �������:
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
	// ��������� ������
	return TridiagonalMatrix();
}

TridiagonalMatrix TridiagonalMatrix::operator*(const TridiagonalMatrix &m)
{
	// ��������� ������
	return TridiagonalMatrix();
}

Vector TridiagonalMatrix::operator*(const Vector &v)
{
	// ��������� ������
	return Vector();
}
