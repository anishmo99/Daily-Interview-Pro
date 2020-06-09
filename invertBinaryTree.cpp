void invertBinaryTree(Node *root)
{
    // base case: if tree is empty
    if (root == nullptr)
        return;

    // invert left subtree
    invertBinaryTree(root->left);

    // invert right subtree
    invertBinaryTree(root->right);
    
    // swap left subtree with right subtree
    swap(root->left, root->right);
}
