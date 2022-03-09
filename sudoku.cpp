#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> board(9,vector<int>(9,0));

int cnt=0;

void f(int row, int col){
	for(int i=1;i<=9;i++){
		int flag=0;
		for(int j=0;j<9;j++){
			if(board[row][j]==i){
				flag=1;
				break;
			}
			else if(board[j][col]==i){
				flag=1;
				break;
			}
			else if(board[row-row%3+j/3][col-col%3+j%3]==i){
				flag=1;
				break;
			}
		}
		if(flag==1)continue;
		board[row][col]=i;
		cnt++;
		if(cnt==81)return;
		int temp=row*9+col+1;
		while(board[temp/9][temp%9]!=0){
			temp++;
		}
		f(temp/9,temp%9);
	}
	if(cnt!=81){
		board[row][col]=0;
		cnt--;
	}
	return;
}

int main(){

	int num;
	int row=9,col=9;
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++){
			cin>>num;
			if(row==9 && num==0){
				row=i;
				col=j;
			}
			if(num!=0)cnt++;
			board[i][j]=num;
		}
	}

	f(row,col);

	cout<<"\n\n";
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}

	return 0;
}