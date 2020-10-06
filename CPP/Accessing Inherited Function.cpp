/* You are given three classes A, B and C. All three classes implement their own version of func.

In class A, func multiplies the value passed as a parameter by :

class A
{
    public:
        A(){
            callA = 0;
        }
    private:
        int callA;
        void inc(){
            callA++;
        }

    protected:
        void func(int & a)
        {
            a = a * 2;
            inc();
        }
    public:
        int getA(){
            return callA;
        }
};
In class B, func multiplies the value passed as a parameter by :

class B
{
    public:
        B(){
            callB = 0;
        }
    private:
        int callB;
        void inc(){
            callB++;
        }
    protected:
        void func(int & a)
        {
            a = a * 3;
            inc();
        }
    public:
        int getB(){
            return callB;
        }
};
In class C, func multiplies the value passed as a parameter by :

class C
{
    public:
        C(){
            callC = 0;
        }
    private:
        int callC;
        void inc(){
            callC++;
        }
    protected:
        void func(int & a)
        {
            a = a * 5;
            inc();
        }
    public:
        int getC(){
            return callC;
        }
};
You are given a class D:

class D 
{

	int val;
	public:
		//Initially val is 1
		 D()
		 {
		 	val = 1;
		 }


		 //Implement this function
		 void update_val(int new_val)
		 {

			
		 }
		 //For Checking Purpose
		 void check(int); //Do not delete this line.
};
You need to modify the class D and implement the function update_val which sets D's val to new_val by manipulating the value by only calling the func defined in classes A, B and C. */

class D :public A, public B, public C
{

	int val;
	public:
		//Initially val is 1
		 D()
		 {
		 	val = 1;
		 }

		 //Implement this function
		 void update_val(int new_val)
		 {
             int *ptr =&val;
             int n=new_val;
            while(val!=new_val)
            {
                if(n%2==0)
                {
                    A::func(*ptr);
                    n=n/2;
                }
                if(n%3==0)
                {
                    B::func(*ptr);
                    n=n/3;
                }
                if(n%5==0)
                {
                    C::func(*ptr);
                    n=n/5;
                }
            }
			
		 }
		 //For Checking Purpose
		 void check(int); //Do not delete this line.
};

void D::check(int new_val)
{
    update_val(new_val);
    cout << "Value = " << val << endl << "A's func called " << getA() << " times " << endl << "B's func called " << getB() << " times" << endl << "C's func called " << getC() << " times" << endl;
}


int main()
{
    D d;
    int new_val;
    cin >> new_val;
    d.check(new_val);

}
