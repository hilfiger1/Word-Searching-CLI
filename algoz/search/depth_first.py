from data_structures.binary_tree import BinaryTree

def pre_order_search(target, root):

    if root:
        if root.data == target:
            return True

        if pre_order_search(target, root.left):
            return True

        if pre_order_search(target, root.right):
            return True

    return False

def post_order_search(target, root):

    if root:
        if post_order_search(target, root.left):
            return True

        if post_order_search(target, root.right):
            return True

        if root.data == target:
            return True

    return False

def in_order_search(target, root):

    if root:
        if in_order_search(target, root.left):
            return True

        if root.data == target:
            return True

        if in_order_search(target, root.right):
            return True

    return False

def search(args):
    bt = BinaryTree()

    print("Building tree...")
    bt.create_from_file(args.file)
    print("...tree built")

    if args.order == "pre-order":
        print("searching tree...")

        target = args.word

        if pre_order_search(target, bt.root):
            print("WORD FOUND")
            return
        else:
            print("WORD NOT FOUND")
            return

    if args.order == "post-order":
        print("searching tree...")

        target = args.word

        if post_order_search(target, bt.root):
            print("WORD FOUND")
            return
        else:
            print("WORD NOT FOUND")
            return

    if args.order == "in-order":
        print("searching tree...")

        target = args.word

        if in_order_search(target, bt.root):
            print("WORD FOUND")
            return
        else:
            print("WORD NOT FOUND")
            return

    print("depth-first-search can only be used with --order 'pre-order', 'post-order', or 'in-order'")