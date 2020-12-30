list_preorder=[]
list_inorder=[]
list_postorder=[]
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.head = None
        self.count=0
    def addToTree(self,val):
        temp = Node(val)
        if self.head:
            iter=self.head
            while iter!=None:
                attr=iter
                if iter.data == val:
                    print("This value exists in the tree.")
                    return
                else:
                    if iter.data<val:
                        iter=iter.right
                    else:
                        iter=iter.left
            if val<attr.data:
                attr.left=temp
            else:
                attr.right=temp
        else:
            self.head = temp
        self.count+=1
    def search(self,val):
        iter=self.head
        if self.head:
            if iter.data == val:
                return True
            else:
                while iter!=None:
                    if val>iter.data:
                        iter=iter.right
                    elif val<iter.data:
                        iter=iter.left
                    else:
                        return True
                return False
        else:
            return False
    def deletion(self,data):
        if self.search(data):
            iter=self.head
            attr=iter
            attr2=iter
            while iter.data!=data:
                attr=iter
                if iter.data>data:
                    iter=iter.left
                else:
                    iter=iter.right
                attr2=iter 
            if iter.left==None and iter.right==None:
                if(iter.data!=self.head.data):
                    if attr.data>data:
                        attr.left=None
                    else:
                        attr.right=None
                else:
                    self.head=None            
            elif iter.left==None and iter.right!=None:
                iter = iter.right
                while iter.left!=None:
                    attr3=iter
                    iter=iter.left
                val = iter.data
                if attr2.right.data==iter.data:
                    attr2.right=None
                else:
                    attr3.left=None
                attr2.data=val
            elif iter.left!=None and iter.right==None:
                iter = iter.left
                while iter.right!=None:
                    attr3=iter
                    iter=iter.right
                val = iter.data
                if attr2.left.data==iter.data:
                    attr2.left=None
                else:
                    attr3.right=None
                attr2.data=val
            elif iter.left!=None and iter.right!=None:
                iter = iter.right
                while iter.left!=None:
                    attr3=iter
                    iter=iter.left
                val = iter.data
                if attr2.right.data==iter.data:
                    attr2.right=None
                else:
                    attr3.left=None
                attr2.data=val
            self.count-=1
            return f"{data} deleted."
        else:
            return f"{data} is not found in tree."             
    def max_min(self,min=False):
        if self.head:
            iter=self.head
            attr=iter
            while iter!=None:
                attr=iter
                if min:
                    iter=iter.left
                else:
                    iter=iter.right
            val=attr.data
            return val
        else:
            return "Tree is empty."
    def predessor(self,data):    # kendisinden küçük en büyük eleman
        iter=self.head
        if self.search(data):
            cur=[]
            while iter.data!=data:
                attr=iter
                if iter.data<data:
                    iter=iter.right
                    cur.append(2)
                else:
                    iter=iter.left
                    cur.append(1)
            if iter.left==None:
                if attr.data<data:
                    return attr.data
                ctrl=len(cur)
                while ctrl>=0:
                    iter=self.head
                    for i in range(ctrl):
                        if cur[i]==2:
                            iter=iter.right
                        else:
                            iter=iter.left
                    if iter.data<data:
                        return iter.data
                    ctrl-=1    
                return data                                         
            else:
                iter=iter.left
                while iter.right!=None:
                    iter=iter.right
                return iter.data
        else:
            return f"{data} is not found in tree."   
    def successor(self,data):     # kendisinden büyük en küçük eleman
        iter=self.head
        if self.search(data):
            cur=[]
            while iter.data!=data:
                attr=iter
                if iter.data<data:
                    iter=iter.right
                    cur.append(2)
                else:
                    iter=iter.left
                    cur.append(1)
            if iter.right==None:
                if attr.data>data:
                    return attr.data
                ctrl=len(cur)
                while ctrl>=0:
                    iter=self.head
                    for i in range(ctrl):
                        if cur[i]==2:
                            iter=iter.right
                        else:
                            iter=iter.left
                    if iter.data>data:
                        return iter.data
                    ctrl-=1
                return data           
            else:
                iter=iter.right
                while iter.left!=None:
                    iter=iter.left
                return iter.data
        else:
            return f"{data} is not found in tree." 
    def preorder(self,root):
        iter=root
        if(iter!=None):
            list_preorder.append(iter.data)
            self.preorder(iter.left)
            self.preorder(iter.right)
    def inorder(self,root):
        iter=root
        if(iter!=None):
            self.inorder(iter.left)
            list_inorder.append(iter.data)
            self.inorder(iter.right)
    def postorder(self,root): 
        iter=root
        if(iter!=None):    
            self.postorder(iter.left)
            self.postorder(iter.right)
            list_postorder.append(iter.data)
    def __len__(self):
        return self.count






