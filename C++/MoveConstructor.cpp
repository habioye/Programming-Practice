#include <iostream>
#include <print>
#include <cstdio>
#include "stdc++.h"

using namespace std;
class Simple {
private:
	int* data;
public:
	// Constructor
	Simple(int value) : data(new int(value))
	{
		cout << "Constructor called, data = " << *data
		<< endl;
	}

	// Destructor
	~Simple()
	{
		delete data;
		cout << "Destructor called" << endl;
	}

	// Copy Constructor
	Simple(Simple& other) :data (other.data) {
	std::cout << "Copy constructor called, data = " << this->data << std::endl;
	}

	// Move constructor
	Simple(Simple&& other)
	: data(other.data)
	{
		// nullify the other object resource
		// This kind of hollows out the object.
		other.data = nullptr;
		cout << "Move constructor called from constructor" << endl;
	}

	// Move assignment operator
	Simple& operator=(Simple&& other)
	{
		if (this != &other) {
			delete data; // Free existing resource
			data = other.data; // Transfer ownership
			other.data = nullptr; // Nullify source
			cout << "Move assignment called from operator" << endl;
		}
		return *this;
	}

	// Disable copy constructor and copy assignment operator
	Simple(const Simple&) = delete;
	Simple& operator=(const Simple&) = delete;

	// Function to print the value
	void print()
	{
		if (data) {
			cout << "Data: " << *data << endl;
		}
		else {
			cout << "Data is null" << endl;
		}
	}

};

int main(int argc, char *argv[]) {
	// Create a Simple object with value 42
	Simple obj1(42);
	obj1.print();

	// Move obj1 to obj2 using move constructor
	Simple obj2 = std::move(obj1);
	// Print obj2's data
	obj2.print();
	// Print obj1's data after move
	obj1.print();

	// Create another Simple object with value 84
	Simple obj3(84);
	// Move obj2 to obj3 using move assignment
	obj3 = std::move(obj2);

	return 0;
}
