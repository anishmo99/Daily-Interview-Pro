/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int depth;
    
    int diameterOfBinaryTree(TreeNode* root) {
        depth = 0;
        
        rec(root);
        
        return depth;
    }
    
    int rec(TreeNode* root){
         if(root == nullptr)
            return 0;
        int l = rec(root->left);
        int r = rec(root->right);
        depth = max(depth, l + r);
        return max(l,r) + 1;
    }
};