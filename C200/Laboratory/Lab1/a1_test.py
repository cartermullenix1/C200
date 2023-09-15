import a1
import unittest

class MyTests(unittest.TestCase):

    def test_c(self):
        self.assertAlmostEqual(a1.c(2,5),62.83,2)
    def test_f(self):    
        self.assertAlmostEqual(a1.f(10),60,2)
    def test_P(self):    
        self.assertAlmostEqual(a1.P(3),80.54,2)  
    def test_seeds(self):    
        self.assertAlmostEqual(a1.seeds(70),0.03,2)   
    def test_D(self):
        self.assertAlmostEqual(a1.D(102,20,5),408,2)   

if __name__=="__main__":
    unittest.main()
