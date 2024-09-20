#include <iostream>
using namespace;

class Node{//b1
	public:
		int PRN;
		string name;
		Node* next;
		Node(int PRN, string name){//b2
			cin>>PRN;
			cin>>name;
			this->PRN = PRN;
			this->name = name;
			next = NULL;
			}//b2
}; //b1

class Pinnacle{//b1

		public:
			Node* head;
			int records;
			Pinnacle(){//b2
				head = NULL;
			}//b2
			
			void insert_at_start(int value);
			void insert_at_location(int value, int location);
			void insert_at_end(int value);
			void del_from_start(void);
			void del_from_end(void);
			void del_from_location(int location);
			void display_LL(void);
}; //b1

void Pinnacle :: insert_at_start(int value){//b1
			}//b1
