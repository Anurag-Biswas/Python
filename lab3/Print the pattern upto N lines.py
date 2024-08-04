def spiral(arr,mat,R,C):
   top=0
   bottom=R-1
   left=0
   right=C-1
   index=0
   while True:
      if(left > right):
         break
      for i in range(left,right+1):
         mat[top][i]=arr[index]
         index+=1
      top+=1
      if (top>bottom):
         break
      for i in range(top,bottom+1):
         mat[i][right]=arr[index]
         index+=1
      right-=1
      if(left>right):
         break
      for i in range(right,left-1,-1):
         mat[bottom][i]=arr[index]
         index+=1
      bottom-=1
      if(top>bottom):
         break
      for i in range(bottom,top-1,-1):
         mat[i][left]=arr[index]
         index+=1
      left+=1
   print("The spiral Matrix is:")
   for i in range(R):
      for j in range(C):
         print(mat[i][j],end=" ")
      print()


N=int(input("Enter the value of N:"))
arr=[]
for i in range(1,N*N+1):
   arr.append(i)
print(arr)
R=N
C=N
mat=[[0 for i in range(C)]for j in range(R)]
spiral(arr,mat,R,C)
