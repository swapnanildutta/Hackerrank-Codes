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

