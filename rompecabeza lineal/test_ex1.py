from datastructures.exercises.linkedlistex1.practice import *
import unittest


class TestPractice(unittest.TestCase):

    def mockuplistA(self):
        #5->7->17->13->11
        listA = LinkedList()
        listA.add(11)
        listA.add(13)
        listA.add(17)
        listA.add(7)
        listA.add(5)
        return listA
    
    def mockuplistB(self):
        #2->10->2->4->6
        listB = LinkedList()
        listB.add(6)
        listB.add(4)
        listB.add(2)
        listB.add(10)
        listB.add(2)
        return listB    

    def test_linked_list_add(self):
        self.assertEqual(5, self.mockuplistA().size())
        self.assertEqual(5, self.mockuplistB().size())

    def test_merging_list_2_into_1(self):
        listA = self.mockuplistA()
        listB = self.mockuplistB()
        listA.merge_alternate(listB)
        self.assertEqual(10, listA.size())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
