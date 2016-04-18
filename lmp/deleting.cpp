Node * delete(Node * root, DataType key) {
    if root == nullptr
        return root
    if key < root.key
        root->left = delete(root->left, key)
    else if key > root.key
        root->right = delete(root->right, key)
    else if root->left != null and root->right != nullptr {
        root.key = minimum(root->right).key
        root->right = delete(root->right, root->right.key)
    }
    else
        if root->left != null
            root = root->left
        else
            root = root->right
    return root
}

Node * minimum(Node * node) {
    if node->left == nullptr
        return node
    return minimum(node->left)
}

http://neerc.ifmo.ru/wiki/index.php?title=%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0,_%D0%BD%D0%B0%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F