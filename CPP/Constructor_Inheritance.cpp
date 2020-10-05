#include<iostream>

using namespace std;

class person {
	string name;
	int code;
	public:
        person() {
            name = "Nil";
            code  = 0;
        }
		person( string a , int b ) {
			name = a;
			code = b;
    	}
		void getdata() { 
            cout<<"\nName: "<<name; 
             cout<<"\nCode: "<<code; 
        }
};

class account : public virtual person {
	int pay;
	public:
		account(int c) {
				pay = c;
			}
    	void getPay(){
            cout<<"\nPay: "<<pay; 
        }
};

class admin : public virtual person {
	string experience;
	public:
		admin(string d)
			{
				experience = d;
			}
			void getExp() { 
                cout<<"\nExperience: "<<experience; 
            }
};

class master: public account, public admin
{
	public:
		master(string a, int b, int c, string d) : account(c), admin(d), person(a, b)
			{
				cout<<"Here are the details.";
			}		
};

int main()
{
	master m( "Oikawa", 211, 1024, "3+ yrs" );
    m.getdata();
    m.getPay();
    m.getExp();
	return 0;
}
