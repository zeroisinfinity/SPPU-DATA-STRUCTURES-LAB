#include <iostream>
using namespace std;

//struct NODE
struct Node{
		int data;
		Node* next;
		};
		
class LinkedList{

		public:
			Node* Head;
			LinkedList():Head(NULL){};
			
			//INSERT AT BEGINNING 
			void insert_at_start(int value);
			void insert_at_location(int value, int location);
			void insert_at_end(int value);
			void del_from_start(void);
			void del_from_end(void);
			void del_from_location(int location);
			void display_LL(void);
			
};

void LinkedList :: insert_at_start(int value){ //bracket-1


		Node* arg_node;
		arg_node = new Node();
		arg_node -> data = value;
		arg_node -> next = Head;
		Head = arg_node;
		
}//bracket-1

void LinkedList :: insert_at_location(int value , int location){ //bracket-1 
		
		//IF LOCATION IS < 1
		if(location < 1){//bracket-2
				cout<<"Location should be greater than or equal to 1"<<endl;
				return ;
                
}//bracket-2
		
		//IF LOCATION IS 1
		if(location == 1){//bracket-3 
				insert_at_start(value);
				return;
}//bracket-3
		Node* arg_node = new Node();
		arg_node -> data = value;
		//arg_node -> next = Head;
		Node* ll_holder = Head;
		
		//IF LINKEDLIST IS EMPTY
		for(int iter = 0; iter < (location - 1 ) && ll_holder ; ++iter){//bracket-4
				ll_holder = ll_holder -> next;
			}//bracket-4

		arg_node -> next = ll_holder -> next;
		ll_holder -> next = arg_node;
		
                
        if(!ll_holder){//b-4
                cout<<"Location out of range."<<endl;
            }//b-4
}//bracket-1

void LinkedList :: insert_at_end(int value){//b1
        
        Node* arg_node = new Node;
        arg_node -> data = value;
        arg_node -> next = NULL;
        
        if(!Head){//b2 
                Head = arg_node;
                return;
            }//b2_
        
        Node* ll_holder = Head;
        while(ll_holder -> next){//b3
            ll_holder = ll_holder -> next;
            }//b3
        ll_holder -> next = arg_node;
}//b1

void LinkedList :: display_LL(void){//b1

        if(!Head){//b2
            cout<<"List is empty"<<endl;
        }//b2

        Node* ll_holder = Head;
        while(ll_holder){//b2
            cout<<ll_holder -> data<<endl;
            ll_holder = ll_holder -> next;
            }//b2
        
}//b1


void LinkedList::del_from_start(void){//b1
		Node* ll_holder = Head -> next;
		free(Head); 
		Head = ll_holder;
		
}//b1
			
void LinkedList :: del_from_location(int location){//b1
		
		if(!Head){//b2
		  	return del_from_start();
		}//b2
		Node* ll_holder = Head;
		for(int travs = 0 ; travs < (location - 1) && ll_holder ; travs++){//b3 
			ll_holder = ll_holder -> next;
			}//b3
		if(!ll_holder){//b3
			cout<<"out of range"<<endl;
		}//b3
		Node* fake_node;
		fake_node -> next = ll_holder -> next;
		ll_holder = fake_node -> next;
		//free(fake_node);
		}//b1

int main() {
    // Initialize a new linked list
    LinkedList list1;

    // Insert elements at the end
    list1.insert_at_end(10);
    list1.insert_at_end(20);

    // Insert element at the beginning
    list1.insert_at_start(5);

    // Insert element at a specific position
    list1.insert_at_location(15, 3);
	list1.del_from_start();
	list1.del_from_location(2);

    cout << "Linked list after insertions: "<<endl;
    list1.display_LL();
return 0;
}
