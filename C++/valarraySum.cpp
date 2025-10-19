#include <iostream>
//#include <bits/stdc++.h> 
#include <valarray>

// C++ program to demonstrate 
// example of sum() function. 


using namespace std; 

int main(int argc, char *argv[]) {
		
	// Initializing valarray 
	valarray<int> varr = { 15, 10, 30, 33, 40 }; 
	
	// Displaying sum of valarray 
	cout << "The sum of valarray is = "
	<< varr.sum() << endl; 
	
	return 0; 
} 
