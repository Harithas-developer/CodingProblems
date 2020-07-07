# # class Node:
# # 	def __init__(self, key):
# # 		self.left = None
# # 		self.right = None
# # 		self.val = key


# # def preorder(root):
# # 	if root:
		
# # 		preorder(root.left)
# # 		preorder(root.right)
# # 		print(root.val)


# # root = Node(1)
# # root.left  = Node(2)
# # root.right = Node(3)
# # root.left.left = Node(4)
# # root.left.right = Node(5)

# # print("preorder function is")
# # preorder(root)















# def shell_sort(arr):
#     sublistcount = len(arr)//2
    
#     # While we still have sub lists
#     while sublistcount > 0:
#         for start in range(sublistcount):
#             # Use a gap insertion
#             gap_insertion_sort(arr,start,sublistcount)

      

#         sublistcount = sublistcount // 2

# def gap_insertion_sort(arr,start,gap):
#     for i in range(start+gap,len(arr),gap):

#         currentvalue = arr[i]
#         position = i

#         # Using the Gap
#         while position>=gap and arr[position-gap]>currentvalue:
#             arr[position]=arr[position-gap]
#             position = position-gap
        
#         # Set current value
#         arr[position]=currentvalue


# arr = [45,67,23,45,21,24,7,2,6,4,90]
# shell_sort(arr)
# print(arr)



def merge_sort(arr):
    
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        print("Left half" , lefthalf)
        print("Right half", righthalf)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
                print("total comparison running", arr)
            else:
                arr[k]=righthalf[j]
                j=j+1
                print("total comparison running", arr)
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1
            print("left comparsion" , arr)


        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
            print("right comparsion" , arr)
        print("total array",arr)




arr = [32,54,21]
merge_sort(arr)
arr