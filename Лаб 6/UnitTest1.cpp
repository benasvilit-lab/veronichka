#include "pch.h"
#include "CppUnitTest.h"
#include "C:\Users\Админ\source\repos\ConsoleApplication1\ConsoleApplication1\Logic1.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(TestMethod1)
		{
			float x = 0.0f;
			float y = 3.0f;
			float s = 0.0f;
			float r = 0.0f;
			float m = 0.0f;
			float expected_s = 0.0f;
			float expected_r = 1.0f;
			Calculate(x, y, s, r, m);

			Assert::AreEqual(expected_r, r, 0.001f, L"r is incorrect");
		}
		TEST_METHOD(TestDivisionByZero) {
			float x = 7.0f;
			float y = 1.0f;
			float s = 0.0f;
			float r = 0.0f;
			float m = 0.0f;
			auto func = [&] { Calculate(x, y, s, r, m); };
			Assert::ExpectException<std::invalid_argument>(func, L"Division by zero");
		}
		TEST_METHOD(TestLessThanZero) {
			float x = 7.0f;
			float y = -4.0f;
			float s = 0.0f;
			float r = 0.0f;
			float m = 0.0f;
			auto func = [&] { Calculate(x, y, s, r, m); };
			Assert::ExpectException<std::invalid_argument>(func, L"The value is less than zero");
		}
	};
}

