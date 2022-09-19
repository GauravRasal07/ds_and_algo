#include <stdio.h>
#include <iostream>
using namespace std;

/*
 *All OOPs concepts are covered in this snippet
*/


/*
Class is blue print of object.
Memory allocated for object is equals to the size of class.
Memory allocated for object of an empty class is 1 byte for the identification of the object.
*/
class Test {

    /*
    Class variables are default declared as private.
    They are not accessible from outside the class.
    They are accessible only from inside the class.
    */
    private:
        int b;

    /*
    Public members of class are accessible globally.
    */
    public:
        int a;
        char c;


    /*
    Static members of class are accessible globally.
    */
        static int time;

        /*
        Constructor is a special member function of class.
        It is called when an object of class is created.
        It is used to initialize the class variables.
        It has the same name as the class.
        It doesn't return any value.
        */

        /*
        When we declare a constructor in a class,
        the default constructor of the class gets overloaded.
        */
        Test()
        {
            cout << "Simple Constructor called" << endl;
        }

    /*
    Parameterized constructor

    */
    Test(int a) {

        /*
        This is pointer containing address of current object.
        */
        this->a = a;
        cout << "Parameterized constructor called" << endl;
    }

    Test(int a, char c){
        this->a = a;
        this->c = c;
        cout << "Parameterized constructor called" << endl;
    }

    /* 
    Copy constructor
    */
    /*
    In copy constructor we pass the adress of the object to be copied as parameter. i.e. &obj(pass by reference)
    If we pass the object to be copied by value, then the copy constructor will get confused and there wiil be infinite loop. 
    */
    Test(Test &obj) {
        this->a = obj.a;
        this->c = obj.c;
        cout << "Copy constructor called" << endl;
    }



    /*
    Getters and setters are the functions used to access and modify the private members of class.
    */
   int getPrivateInt(){
       return b;
   }

   void setPrivateInt(int b){
       this->b = b;
   }


    /* 
    Static member function
    Static functions can acces static members of the class only.
    They doesn't have this pointer.
    They can't access non static members of the class.
    */
    static void staticFunc(){
        cout << "Time is: " << time << endl;
        cout << "Static function called" << endl;
    }



    /*
    Destructor is a special member function of class.
    It is called when an object of class is destroyed.
    It is used to free the memory allocated(memory de-allocation) for the class variables.
    It has the same name as the class.
    It doesn't return any value.
    */
    ~Test() {
        cout << "Simple Destructor called" << endl;
    }

};

/*
Initalizing static members of class
*/
int Test::time = 5;     // :: is used to access static members of class(scope resolution operator)


/*  HOME WORK
Initialization List
const keyword is used to initialize the class variables.
*/


int main(){

    /* 
    Calling static member function 
    It doesn't require object of class.
    */
    Test::staticFunc();

    /* 
    Object is instance of class
    */
    Test t;                     //static memory allocation for object t
    /*
    Destructor for static memory allocation is called automatically when the program ends.
    */

    Test *t2 = new Test();      //dynamic memory allocation for object t1
    delete t2;
    /*
    Destructor for dynamic memory allocation is not called automatically.
    We have to call it explicitly.
    */

    Test *t1 = new Test(10);    //dynamic memory allocation for object t2 and calling parameterized constructor

    Test *t3 = new Test(10, 'a');


    /*
    All the values of object t3 are copied into object copy using default copy constructor.
    Default copy constructor copies all values using shallow copy.
    i.e. it copies the address of the object.
    So, if you modify the value of any member of object t3,
    it will also modify the value of the same member of object copy.
    */
    Test *copy = new Test(*t3);  //copying object t3 into object copy


    /*
    We can deep copy all the values using user defined copy constructor.
    In this case, we create different variables for each object. 
    */

    Test *copy1(t3);            //copy constructor is called


    /*
    Copy assignment operator copies all values of the right hand side object into the left hand side object.
    */
    t3 = t2;




    /*
    Members of class are accessed using dot operator.
    Members of class object which is created using new operator are accessed using arrow operator.
    Also members of class object which is created using new operator are accessed using dot operator by dereferencing the pointer.
    */
    t.a = 10;
    cout << "Public integer: " << t.a << endl;

    t.setPrivateInt(20);
    cout << "Private integer: " << t.getPrivateInt() << endl;

    t1->a = 30;
    cout << "Public integer: " << t1->a << endl;

    t1->setPrivateInt(40);
    cout << "Private integer: " << t1->getPrivateInt() << endl;


    /*
    Padding is done to make sure that the object is aligned to the memory address.
    i.e. the memory address is multiple of 8.
    Greedy alignment is also done to make sure that the object is aligned to the memory address.
    */
    cout << "Size of class: " << sizeof(Test) << endl;


    return 0;
}