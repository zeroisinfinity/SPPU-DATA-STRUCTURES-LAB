#include <iostream>
using namespace;

class Node{//b1
	public:
		int PRN;
		string name;
		Node* next;
		Node(int PRN, string name){//b2
			this->PRN = PRN;
			this->name = name;
			next = NULL;
			}//b2
}; //b1

class Pinnacle{//b1

		public:
			Node* prez;
			int div_size;
			Pinnacle(){//b2
				prez = NULL;
			}//b2
			
			void appoint_prez(int value,string data);
			void appoint_memb(int value , string data, int location);
			void appoint_sect(int value , string data);
			void remove_prez(void);
			void remove_memb(int location);
			void remove_sect(void);
			void display_div(void);
}; //b1

void Pinnacle :: appoint_prez(int value,string data){//b1
      
			Node* arg_node;
			arg_node = new Node(value,data);
			arg_node -> next = prez;
			prez = arg_node;
			
			}//b1
		
void Pinnacle ::appoint_memb(int value , string data ,int location){//b1

			if(location<=1){//b2
				cout<<"Location should be greater than 1."<<endl;
					}//b2

      
			
			
			ll_holder = prez;
			for(int trav = 1 ; trav < location && ll_holder ; trav++){//b3
				ll_holder = ll_holder -> next;
				}//b3
			arg_node = new Node(value,data);
			ll_holder -> next = arg_node;
			
			
				}//b1
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
