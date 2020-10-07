struct TrieNode
{
    TrieNode* child[26];
    bool unique;

    TrieNode()
    {
        unique = true;
        for (int i = 0; i < 26; i++)
            child[i] = nullptr;
    }
};

void makeTrie(TrieNode *root, string s)
{
    TrieNode *cur = root;

    int i = 0;
    while (i < s.size())
    {
        if (cur->child[s[i] - 'a'] == nullptr){
            TrieNode* node = new TrieNode();
            cur->child[s[i] - 'a'] = node;
        }
        else
            cur->child[s[i] - 'a']->unique = false;

        cur = cur->child[s[i] - 'a'];
        i++;
    }
}

string findPrefix(TrieNode *root, string s)
{
    if (s.empty())
        return "";

    string temp;

    TrieNode *cur = root;

    int i = 0;

    do
    {
        cur = cur->child[s[i] - 'a'];
        temp.push_back(s[i]);
        i++;
    } while (i < s.size() and !cur->unique);

    return temp;
}

vector<string> Solution::prefix(vector<string> &A)
{
    TrieNode *root = new TrieNode();

    vector<string> sol;

    for (int i = 0; i < A.size(); i++)
    {
        makeTrie(root, A[i]);
    }

    for (int i = 0; i < A.size(); i++)
    {
        sol.push_back(findPrefix(root, A[i]));
    }

    return sol;
}
