#include "TridiagonalMatrix.h"


void main()
{
	Cell a[4]={1,2,1,2};
	Vector A(4, a);

	Cell b[4]={2,2,0,1};
	Vector B(4, b);

	Vector C = A+B;
	cout
		<< "\nA =\n" << A
		<< "\nB =\n" << B
		<< "\nA + B =\n" << C;

	cin.get();
}
