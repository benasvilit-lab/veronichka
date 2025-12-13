#include <iostream>
#include "Logic1.h"

using namespace std;

int main()
{
    float x, y, s, r, m;

    cout << "x = ";
    cin >> x;
    cout << "y = ";
    cin >> y;

    try {
       float res = Calculate(x, y, s, r, m);
        cout << "s = " << s << endl;
    cout << "r = " << r << endl;
    cout << "c = " << m << endl;
    }
    catch (const invalid_argument& e) {
        cout << "ERROR: " << e.what() << endl;
    }

    system("pause");
    return 0;
}