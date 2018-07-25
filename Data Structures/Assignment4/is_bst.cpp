#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int key;
    int left;
    int right;
    
    Node() : key(0), left(-1), right(-1) {}
    Node(int key_, int left_, int right_) : key(key_), left(left_), right(right_) {}
};

class Helper {
private:
    vector<int> res;
    vector<Node>& Tree;
public:
    Helper(vector<Node>& tree) : Tree(tree) {}
    void inOrderTraverse(int i) {
        if (Tree[i].left != -1) {
            inOrderTraverse(Tree[i].left);
        }
        res.push_back(Tree[i].key);
        if (Tree[i].right != -1) {
            inOrderTraverse(Tree[i].right);
        }
    }
    bool IsBinarySearchTree() {
        res.clear();
        inOrderTraverse(0);
        for (int i = 0; i < (int)res.size() - 1; i++) {
            if (res[i] > res[i + 1]) {
                return false;
            }
        }
        return true;
    }
};



int main() {
    int nodes;
    cin >> nodes;
    if (nodes <= 1 && nodes >= 0) {
        cout << "CORRECT";
        return 0;
    }
    vector<Node> tree;
    for (int i = 0; i < nodes; ++i) {
        int key, left, right;
        cin >> key >> left >> right;
        tree.push_back(Node(key, left, right));
    }
    Helper helper = Helper(tree);
    if (helper.IsBinarySearchTree()) {
        cout << "CORRECT" << endl;
    } else {
        cout << "INCORRECT" << endl;
    }
    return 0;
}
