import random


class AVLNode(object):
    """
    A class representing a node in an AVL tree
    """

    def __init__(self, value, is_real=True):
        """
        Constructor, you are allowed to add more fields.

        @type value: str or None
        @param value: data of your node
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0 if is_real else -1
        self.isReal = is_real
        self.size = 1 if self.isReal else 0

    def getLeft(self):
        """
        returns the left child

        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child
        """
        return self.left

    def getRight(self):
        """
        returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child
        """
        return self.right

    def getParent(self):
        """
        returns the parent 

        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        """
        return self.parent

    def getValue(self):
        """
        return the value

        @rtype: str
        @returns: the value of self, None if the node is virtual
        """
        return self.value

    def getHeight(self):
        """
        returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """
        return self.height

    def getBalanceFactor(self):
        """
        returns the balance factor

        @pre: self.isRealNode() is True   
        @rtype: int
        @returns: the balance factor of self
        """
        return self.getLeft().getHeight() - self.getRight().getHeight()

    def getSize(self):
        """
        returns the size

        @rtype: int
        @returns: the size of self, 0 if the node is virtual
        """
        return self.size

    def setLeft(self, node):
        """
        sets left child and sets node's parent accordingly.

        @type node: AVLNode or None
        @param node: a node
        """
        self.left = node
        node.setParent(self)

    def setRight(self, node):
        """
        sets right child and sets node's parent accordingly.

        @type node: AVLNode or None
        @param node: a node
        """
        self.right = node
        node.setParent(self)

    def setParent(self, node):
        """
        sets parent

        @type node: AVLNode or None
        @param node: a node
        """
        self.parent = node

    def setValue(self, value):
        """
        sets value

        @type value: str or None
        @param value: data
        """
        self.value = value

    def setHeight(self, h):
        """
        sets the height  of the node

        @type h: int
        @param h: the height
        """
        self.height = h

    def setSize(self, s):
        """
        sets the size of the node

        @type s: int
        @param s: the size
        """
        self.size = s

    def isRealNode(self):
        """
        returns whether self is not a virtual node 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        return self.isReal

    def isLeaf(self):
        """
        returns whether self is a leaf 

        @rtype: bool
        @returns: True if self is a leaf, False otherwise.
        """
        return self.getHeight() == 0

    def add_virtual_children(self):
        """
        set children to be virtual nodes
        """
        self.setLeft(AVLNode(None, False))
        self.setRight(AVLNode(None, False))

    def calc_height(self):
        """
        calculates self's height according to its children
        
        @pre: self.isRealNode() is True
        @rtype: int
        @returns: the height of self
        """
        return max(self.getLeft().getHeight(), self.getRight().getHeight()) + 1

    def calc_size(self):
        """
        calculates self's size according to its children

        @pre: self.isRealNode() is True
        @rtype: int
        @returns: the size of self
        """
        return self.getLeft().getSize() + self.getRight().getSize() + 1

    def fix_node_height_and_size(self):
        """
        sets height and size of self according to its children

        @pre: self.isRealNode() is True
        """
        self.setSize(self.calc_size())
        self.setHeight(self.calc_height())

    def get_predecessor(self):
        """
        returns the predecessor of node in the list

        @rtype: AVLNode
        @returns: the predecessor of node in the list
        """
        if self.getLeft().isRealNode():
            return self.getLeft().find_last_node()
        node = self
        parent_node = node.getParent()
        while parent_node is not None and node == parent_node.getLeft():  # node is Parent_node left child
            node = parent_node
            parent_node = node.getParent()
        return parent_node

    def get_successor(self):
        """
        returns the successor of node in the list

        @rtype: AVLNode
        @returns: the successor of node in the list
        """
        if self.getRight().isRealNode():
            return self.getRight().find_first_node()
        node = self
        parent_node = node.getParent()
        while parent_node is not None and node == parent_node.getRight():  # node is Parent_node right child
            node = parent_node
            parent_node = node.getParent()
        return parent_node

    def find_first_node(self):
        """
        returns the first node in the subtree rooted with self

        @rtype: AVLNode
        @returns: the first node in the subtree rooted with self
        """
        node = self
        while node.getLeft().isRealNode():
            node = node.getLeft()
        return node

    def find_last_node(self):
        """
        returns the last node in the subtree rooted with self

        @rtype: AVLNode
        @returns: the last node in the subtree rooted with self
         """
        node = self
        while node.getRight().isRealNode():
            node = node.getRight()
        return node

    def update_node_fields(self, right_child, left_child, parent):
        """
        update self fields and fixes its height and size accordingly

         @type right_child: AVLNode
         @param right_child: a node represents the new right child of self
         @type left_child: AVLNode
         @param left_child: a node represents the new left child of self
         @type parent: AVLNode or None
         @param parent: a node represents the new parent of self
         """
        self.setRight(right_child)
        self.setLeft(left_child)
        self.setParent(parent)
        self.fix_node_height_and_size()


class AVLTreeList(object):
    """
    A class implementing the ADT list, using an AVL tree.
    """

    def __init__(self):
        """
        Constructor, you are allowed to add more fields.
        """
        self.size = 0
        self.root = None
        self.first_node = None
        self.last_node = None

    def update_tree_fields(self, root, first_node, last_node):
        """
        update self fields

        @type root: AVLNode or None
        @param root: a node represents the new root of self
        @type first_node: AVLNode or None
        @param first_node: a node represents the new first_node of self
        @type last_node: AVLNode or None
        @param last_node: a node represents the new last_node of self
        """
        self.set_root(root)
        self.set_size(0 if root is None else root.getSize())
        self.set_first_node(first_node)
        self.set_last_node(last_node)

    def empty(self):
        """
        returns whether the list is empty

        @rtype: bool
        @returns: True if the list is empty, False otherwise
        """
        return self.getSize() == 0

    def retrieve_node(self, i):
        """
        retrieves the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length() 
        @param i: index in the list
        @rtype: AVLNode
        @returns: the i'th item in the list
        """
        def retrieve_rec(node, k):
            r = node.getLeft().getSize() + 1
            if r == k:
                return node
            elif r > k:
                return retrieve_rec(node.left, k)
            return retrieve_rec(node.right, k - r)

        return retrieve_rec(self.getRoot(), i + 1)

    def retrieve(self, i):
        """
        retrieves the value of the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: str
        @returns: the value of the i'th item in the list
        """
        if 0 <= i <= self.size - 1:
            return self.retrieve_node(i).getValue()
        return None

    def insert(self, i, val):
        """
        inserts val at position i in the list

        @type i: int
        @pre: 0 <= i <= self.length()
        @param i: The intended index in the list to which we insert val
        @type val: str
        @param val: the value we insert
        @rtype: int
        @returns: the number of re-balancing operation due to AVL re-balancing
        """
        node = AVLNode(val)
        node.add_virtual_children()
        if self.empty():
            self.update_tree_fields(node, node, node)
            return 0
        if i == self.length():
            self.get_last_node().setRight(node)
            self.set_last_node(node)
        else:
            if i == 0:
                self.set_first_node(node)  # Updating self.first
            prev_i_node = self.retrieve_node(i)
            if prev_i_node.getLeft().isRealNode() is False:  # Case 1: prev_node doesn't have left son
                prev_i_node.setLeft(node)
            else:  # Case 2: prev_node has left son
                node_predecessor = prev_i_node.get_predecessor()
                node_predecessor.setRight(node)

        return self.fix_the_tree(node, False)

    def fix_the_tree(self, starting_node, fix_to_the_root):
        """
        Re-balancing the tree after insertion/deletion

        @type starting_node: AVLNode
        @param starting_node: The node to be inserted or physically deleted
        @type fix_to_the_root: bool
        @param fix_to_the_root: False if re-balancing after insertion, True if re-balancing after deletion 
        @rtype: int
        @returns: the number of re-balancing operation due to AVL re-balancing
        """
        rotations_count = 0
        y = starting_node.getParent()
        while y is not None:
            y_old_height = y.getHeight()
            y.setHeight(y.calc_height())
            balance_factor = y.getBalanceFactor()
            if abs(balance_factor) < 2 and y.getHeight() == y_old_height:
                break
            elif abs(balance_factor) < 2 and y.getHeight() != y_old_height:
                y = y.getParent()
                continue
            y_parent = y.getParent()
            rotations_count += self.perform_rotation(y)
            if fix_to_the_root is False:
                break
            y = y_parent
        self.fix_tree_nodes_height_and_sizes(starting_node)
        return rotations_count

    def perform_rotation(self, bf_criminal):
        """
        performs rotation on bf_criminal according to its and its child's BF 

        @type bf_criminal: AVLNode
        @param bf_criminal: the node to be rotated
        """
        if bf_criminal.getBalanceFactor() == 2:
            if bf_criminal.getLeft().getBalanceFactor() == -1:
                self.left_rotation(bf_criminal.getLeft())
                self.right_rotation(bf_criminal)
                return 2
            self.right_rotation(bf_criminal)
            return 1
        if bf_criminal.getRight().getBalanceFactor() == 1:
            self.right_rotation(bf_criminal.getRight())
            self.left_rotation(bf_criminal)
            return 2
        self.left_rotation(bf_criminal)
        return 1

    def left_rotation(self, node_a):
        """
        performs left rotation on node_b and its right child and fixes its size and height 

        @type node_a: AVLNode
        @param node_a: the node to be rotated with his child
        """
        node_b = node_a.getRight()
        node_a_parent = node_a.getParent()
        node_a.setRight(node_b.getLeft())
        node_b.setLeft(node_a)
        if node_a_parent is not None:
            if node_a_parent.getRight() == node_a:
                node_a_parent.setRight(node_b)
            else:
                node_a_parent.setLeft(node_b)
        else:
            node_b.setParent(None)
            self.set_root(node_b)

        node_a.fix_node_height_and_size()
        node_b.fix_node_height_and_size()

    def right_rotation(self, node_b):
        """
        performs right rotation on node_b and its left child and fixes its size and height 

        @type node_b: AVLNode
        @param node_b: the node to be rotated with his child
        """
        node_a = node_b.getLeft()
        node_b_parent = node_b.getParent()
        node_b.setLeft(node_a.getRight())
        node_a.setRight(node_b)
        if node_b_parent is not None:
            if node_b_parent.getRight() == node_b:
                node_b_parent.setRight(node_a)
            else:
                node_b_parent.setLeft(node_a)
        else:
            node_a.setParent(None)
            self.set_root(node_a)

        node_b.fix_node_height_and_size()
        node_a.fix_node_height_and_size()

    def fix_tree_nodes_height_and_sizes(self, starting_node):
        """
        fixes all nodes height and size from starting_node all the way to the root

        @type starting_node: AVLNode
        @param starting_node: the first node to fix its height and size
        """
        y = starting_node.getParent()
        node = starting_node
        if node.isRealNode():
            node.fix_node_height_and_size()
        while y is not None:
            y.fix_node_height_and_size()
            y = y.getParent()
        self.set_size(self.getRoot().getSize())

    def delete(self, i):
        """deletes the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: The intended index in the list to be deleted
        @rtype: int
        @returns: the number of re-balancing operation due to AVL re-balancing
        """
        if self.empty():
            return -1
        if self.length() == 1:
            self.update_tree_fields(None, None, None)
            return 0
        node_to_delete = self.retrieve_node(i)
        physically_deleted_node = node_to_delete
        if i == 0:
            self.set_first_node(node_to_delete.get_successor())
        if i == self.length() - 1:
            self.set_last_node(node_to_delete.get_predecessor())
        if node_to_delete.isLeaf():  # Case 1: leaf
            self.replace_node(node_to_delete, AVLNode(None, False), False)
        elif node_to_delete.getRight().isRealNode() is False or node_to_delete.getLeft().isRealNode() is False:
            # Case 2: has only 1 child
            node_to_delete_son = node_to_delete.getRight() \
                if node_to_delete.getRight().isRealNode() else node_to_delete.getLeft()
            self.replace_node(node_to_delete, node_to_delete_son, False)
        else:  # Case 3: has 2 children
            node_to_delete_suc = node_to_delete.get_successor()
            node_to_delete_suc_parent = node_to_delete_suc.getParent()
            self.replace_node(node_to_delete_suc, node_to_delete_suc.getRight(), False)
            self.replace_node(node_to_delete, node_to_delete_suc, True)
            physically_deleted_node = node_to_delete_suc_parent.getLeft()
        return self.fix_the_tree(physically_deleted_node, True)

    def replace_node(self, node_to_be_replaced, new_node, has_two_children):
        """
        replace node_to_be_replaced with new_node

        @type node_to_be_replaced: AVLNode
        @param node_to_be_replaced: the node that will be replaced
        @type new_node: AVLNode
        @param new_node: the node that will replace node_to_be_replaced 
        @type has_two_children: bool
        @param has_two_children: True if node_to_be_replaced has 2 children, False otherwise
        """
        if node_to_be_replaced == self.root:
            self.set_root(new_node)
            new_node.setParent(None)
        elif node_to_be_replaced.getParent().getRight() == node_to_be_replaced:
            node_to_be_replaced.getParent().setRight(new_node)
        else:
            node_to_be_replaced.getParent().setLeft(new_node)
        if has_two_children:
            new_node.setRight(node_to_be_replaced.getRight())
            new_node.setLeft(node_to_be_replaced.getLeft())
            new_node.setHeight(node_to_be_replaced.getHeight())
            new_node.setSize(node_to_be_replaced.getSize())

    def first(self):
        """
        returns the value of the first item in the list

        @rtype: str
        @returns: the value of the first item, None if the list is empty
        """
        return None if self.empty() else self.get_first_node().getValue()

    def last(self):
        """
        returns the value of the last item in the list

        @rtype: str
        @returns: the value of the last item, None if the list is empty
        """
        return None if self.empty() else self.get_last_node().getValue()

    def listToArray(self):
        """
        returns an array representing list 

        @rtype: list
        @returns: a list of strings representing the data structure
        """
        def list_to_array_rec(node, lst):
            if node.isRealNode() is False:
                return
            list_to_array_rec(node.getLeft(), lst)
            lst.append(node.getValue())
            list_to_array_rec(node.getRight(), lst)
            return lst

        return [] if self.empty() else list_to_array_rec(self.root, [])

    def length(self):
        """
        returns the size of the list 

        @rtype: int
        @returns: the size of the list
        """
        return self.getSize()

    @staticmethod
    def merge(lst1, lst2):
        """
        returns one sorted list containing the elements of both lists A and B

        @type lst1: list
        @pre: A is i1 sorted list
        @param lst1: the first list 
        @type lst2: list
        @pre: B is i1 sorted list
        @param lst2: the second list 
        @rtype: List
        @returns: sorted list contained A & B elements
        """
        n = len(lst1)
        m = len(lst2)
        merged = [None] * (n+m)
        i1 = i2 = j = 0
        while i1 < n and i2 < m:
            if lst1[i1] < lst2[i2]:
                merged[j] = lst1[i1]
                i1 += 1
            else:
                merged[j] = lst2[i2]
                i2 += 1
            j += 1
        if i1 == n:
            while i2 < m:
                merged[j] = lst2[i2]
                i2 += 1
                j += 1
        else:
            while i1 < n:
                merged[j] = lst1[i1]
                i1 += 1
                j += 1
        return merged

    @staticmethod
    def mergesort(lst, start_index, end_index):
        """
        returns sorted lst

        @type lst: list
        @param lst: the list to be sorted
        @type start_index: int
        @param start_index: the start index from which to sort
        @type end_index: int
        @param end_index: the end index from which to sort
        @rtype: List
        @returns: sorted lst between start and wnd indexes
        """
        n = end_index - start_index
        if n <= 1:
            return [lst[start_index]]
        else:
            lst1 = AVLTreeList.mergesort(lst, start_index, start_index + (n // 2))
            lst2 = AVLTreeList.mergesort(lst, start_index + (n // 2), end_index)
        return AVLTreeList.merge(lst1, lst2)

    @staticmethod
    def create_tree_from_list(lst, begin_index, end_index):
        """
        returns AVLNode represents the root of a tree, which linked to all other lst elements represented as AVLNodes 

        @type lst: List
        @param lst: list of AVLNode's values
        @type begin_index: int
        @param begin_index: start index in lst to create the tree from
        @type end_index: int
        @param end_index: end index in lst to create the tree from
        @rtype: AVLNode
        @returns: AVLNode represents the root of a tree, which linked to all other lst elements represented as AVLNodes 
        """
        if end_index - begin_index == 1:
            new_node = AVLNode(lst[begin_index])
            new_node.add_virtual_children()
            return new_node
        if end_index == begin_index:
            return AVLNode(None, False)
        median_index = begin_index + ((end_index - begin_index) // 2)
        median_node = AVLNode(lst[median_index])
        median_node.setLeft(AVLTreeList.create_tree_from_list(lst, begin_index, median_index))
        median_node.setRight(AVLTreeList.create_tree_from_list(lst, median_index + 1, end_index))
        median_node.fix_node_height_and_size()
        return median_node

    @staticmethod
    def make_tree_from_list(lst):
        """
        returns an AVLTreeList containing all elements in lst  

        @type lst: list
        @param lst: the list to be "converted" to an AVLTreeList
        @rtype: AVLTreeList
        @returns: an AVLTreeList containing all elements in lst
        """
        if len(lst) == 0:
            return AVLTreeList()
        lst_root = AVLTreeList.create_tree_from_list(lst, 0, len(lst))
        new_tree = AVLTreeList()
        first_node = lst_root.find_first_node()
        last_node = lst_root.find_last_node()
        new_tree.update_tree_fields(lst_root, first_node, last_node)
        return new_tree

    def sort(self):
        """
        sort the info values of the list

        @rtype: list
        @returns: an AVLTreeList where the values are sorted by the info of the original list.
        """
        lst_tree = self.listToArray()
        lst_without_none = [lst_tree[i] for i in range(len(lst_tree)) if lst_tree[i] is not None]
        none_count = len(lst_tree) - len(lst_without_none)
        sorted_lst = []
        if none_count != len(lst_tree):
            sorted_lst = AVLTreeList.mergesort(lst_without_none, 0, len(lst_without_none))
        for i in range(none_count):
            sorted_lst.append(None)
        return AVLTreeList.make_tree_from_list(sorted_lst)

    def permutation(self):
        """
        permute the info values of the list 

        @rtype: list
        @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. Use Randomness
        """
        lst_tree = self.listToArray()
        for i in range(len(lst_tree) - 1, 0, -1):
            random_element_index = random.randint(0, i)
            lst_tree[i], lst_tree[random_element_index] = lst_tree[random_element_index], lst_tree[i]
        return AVLTreeList.make_tree_from_list(lst_tree)

    @staticmethod
    def concat_helper(higher_tree, lower_tree, self_is_higher, mid_node):
        """
        concatenates lower_tree to higher_tree if self_is_higher is True. otherwise, concatenates higher_tree to 
        lower_tree 

        @type higher_tree: AVLTreeList
        @param higher_tree: a list
        @type lower_tree: AVLTreeList
        @param lower_tree: a list
        @type self_is_higher: bool
        @param self_is_higher: True if higher_tree is self, False otherwise
        @type mid_node: AVLNode
        @param mid_node: AVLNode which all keys of one tree are smaller than him, and all keys of the second tree are
                         bigger than him
        @rtype: AVLNode
        @returns: the first node in the concatenated list that is BF criminal suspect
        """
        node = higher_tree.getRoot()
        while node.getHeight() > lower_tree.getRoot().getHeight():
            node = node.getRight() if self_is_higher else node.getLeft()
        node_parent = node.getParent()
        if self_is_higher:
            node_parent.setRight(mid_node)
            mid_node.setRight(lower_tree.getRoot())
            mid_node.setLeft(node)
            higher_tree.set_last_node(lower_tree.get_last_node())
        else:
            node_parent.setLeft(mid_node)
            mid_node.setLeft(lower_tree.getRoot())
            mid_node.setRight(node)
            lower_tree.update_tree_fields(higher_tree.getRoot(), lower_tree.get_first_node(),
                                          higher_tree.get_last_node())
        return node

    def concat_empty_trees(self, lst):
        """
        concatenates lst to self when one/two of them is empty

        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """
        if self.empty() and lst.empty():
            return 0
        if self.empty():
            self.update_tree_fields(lst.getRoot(), lst.get_first_node(), lst.get_last_node())
        return self.getRoot().getHeight() + 1

    def concat_trees_with_one_element(self, lst):
        """
        concatenates lst to self when one/two of them has one element

        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        """
        if lst.size == 1:
            self.get_last_node().setRight(lst.getRoot())
            self.set_last_node(lst.getRoot())
            self.fix_the_tree(self.get_last_node(), False)
        elif self.getSize() == 1:  # lst.length() > 1
            lst_first = lst.get_first_node()
            lst.delete(0)
            node = AVLTreeList.concat_helper(lst, self, False, lst_first)
            self.fix_the_tree(node, True)

    def concat(self, lst):
        """
        concatenates lst to self

        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """
        self_last = self.get_last_node()
        if self.empty() or lst.empty():  # Case 1: one of the lists is empty
            return self.concat_empty_trees(lst)
        return_val = abs(lst.getRoot().getHeight() - self.getRoot().getHeight())
        if lst.getSize() == 1 or self.getSize() == 1:  # Case 2: one of the lists has only one element
            self.concat_trees_with_one_element(lst)
            return return_val
        #  Case 3: both lists has more than one element
        self.delete(self.length() - 1)
        lst_height = lst.getRoot().getHeight()
        self_height = self.getRoot().getHeight()
        if abs(self_height - lst_height) < 2:  # Case 3.1: |height difference| <= 1
            self_last.update_node_fields(lst.getRoot(), self.getRoot(), None)
            self.update_tree_fields(self_last, self.get_first_node(), lst.get_last_node())
            return return_val
        elif self_height > lst_height:  # Case 3.2: self is higher than lst
            node = AVLTreeList.concat_helper(self, lst, True, self_last)
        else:  # Case 3.3: lst is higher than self
            node = AVLTreeList.concat_helper(lst, self, False, self_last)
        self.fix_the_tree(node, True)
        return return_val

    def search(self, val):
        """
        searches for a *value* in the list

        @type val: str
        @param val: a value to be searched
        @rtype: int
        @returns: the first index that contains val, -1 if not found.
        """
        tree_as_lst = self.listToArray()
        for i in range(len(tree_as_lst)):
            if tree_as_lst[i] == val:
                return i
        return -1

    def getRoot(self):
        """
        returns the root of the tree representing the list

        @rtype: AVLNode
        @returns: the root, None if the list is empty
        """
        return self.root

    def set_root(self, root):
        """
        set root to be the new root of self

        @type root: AVLNode
        @param root: new root to be set
        """
        self.root = root

    def getSize(self):
        """
        returns the size of the tree representing the list

        @rtype: int
        @returns: the size of the tree
        """
        return self.size

    def set_size(self, size):
        """
        set size to be the new size of self

        @type size: int
        @param size: new size of self
        """
        self.size = size

    def get_first_node(self):
        """
        returns the first node of the tree representing the list

        @rtype: AVLNode
        @returns: the first node of the tree
        """
        return self.first_node

    def set_first_node(self, first_node):
        """
        set first_node to be the new first_node of self

        @type first_node: AVLNode
        @param first_node: new first_node of self
        """
        self.first_node = first_node

    def get_last_node(self):
        """
        returns the last node of the tree representing the list

        @rtype: AVLNode
        @returns: the last node of the tree
        """
        return self.last_node

    def set_last_node(self, last_node):
        """
        set last_node to be the new last_node of self

        @type last_node: AVLNode
        @param last_node: new last_node of self
        """
        self.last_node = last_node
        
