#pragma once
#include <cmath>
#include <algorithm>
#include <stdexcept>

using namespace std;

inline float Calculate(float x, float y, float& s, float& r, float& m) {
	if (y == 1) {
		throw invalid_argument("Division by zero");
	}
	if (y <= 0) {
		throw invalid_argument("The value is less than zero");
	}
	r = pow((x + y), 3 * sin(x));
	s = sqrt(abs(x)) / log(y);
	m = max(r, s);
}
