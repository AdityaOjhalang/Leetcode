# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Initialize the stack with the nestedList reversed, so we can simulate left-to-right traversal
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # When next() is called, the top of the stack is guaranteed to be an integer (because of hasNext())
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        # Keep processing until we find an integer on top or stack becomes empty
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # Otherwise, top is a list, so we need to expand it
            self.stack.pop()
            nested = top.getList()
            # Push all elements of the nested list in reverse order so that the leftmost element is on top
            for item in reversed(nested):
                self.stack.append(item)
        return False
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())