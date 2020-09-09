class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
    	vector<vector<int>> result;
    	queue<TreeNode*> q;
    	q.push(root);
    	while(!q.empty()){
    		int n = q.size();
    		vector<int> current_level;
    		for(int i = 0; i < n; i++){
    			TreeNode* temp = q.front();
    			q.pop();
    			if(temp != nullptr){
    				current_level.push_back(temp->val);
    				q.push(temp->left);
    				q.push(temp->right);
    			}
    		}
    		if(current_level.size() > 0)
    			result.emplace_back(current_level);
    	}
    	return result;
    }
};