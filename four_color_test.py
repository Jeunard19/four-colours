import unittest
import four_color

class Test(unittest.TestCase):

    def test_create_bording_region_dict(self):
        adj = [
        [ 0, 1, 1, 1, 0 ],
        [ 1, 0, 1, 0, 0 ],
        [ 1, 1, 0, 1, 0 ], 
        [ 1, 0, 1, 0, 1 ], 
        [ 0, 0, 0, 1, 0 ]  
        ]
        bording_region_dict = four_color.create_bording_region_dict(adj)
        self.assertEqual(bording_region_dict["Region_0"], {"Region_1","Region_2","Region_3"}, 'Bording region for Region_0 do not match.')
        self.assertEqual(bording_region_dict["Region_1"], {"Region_0","Region_2"}, 'Bording region for Region_1 do not match.')
        self.assertEqual(bording_region_dict["Region_2"], {"Region_0","Region_1","Region_3"}, 'Bording region for Region_2 do not match.')
        self.assertEqual(bording_region_dict["Region_3"], {"Region_0","Region_2","Region_4"}, 'Bording region for Region_3 do not match.')
        self.assertEqual(bording_region_dict["Region_4"], {"Region_3"}, 'Bording region for Region_4 do not match.')
        self.assertEqual(len(bording_region_dict), len(adj), 'Incorrect number of regions')
    
    def test_create_initial_results_dict(self):
        bording_region_dict={'Region_0': {}, 'Region_1': {}, 'Region_2': {}, 'Region_3': {}, 'Region_4': {}}
        initial_results_dict = four_color.create_initial_results_dict(bording_region_dict)
        self.assertEqual(initial_results_dict, {'Region_0': 0, 'Region_1': 0, 'Region_2': 0, 'Region_3': 0, 'Region_4': 0}, 'All initial region values should be 0')
        
    def test_allocate_color(self):
        bording_region_dict={'Region_0': {'Region_3', 'Region_2', 'Region_1'}, 'Region_1': {'Region_2', 'Region_0'}, 'Region_2': {'Region_3', 'Region_1', 'Region_0'},
         'Region_3': {'Region_2', 'Region_4', 'Region_0'}, 'Region_4': {'Region_3'}}
        
        results_dict={'Region_0': 1, 'Region_1': 1, 'Region_2': 1, 'Region_3': 1, 'Region_4': 1}
        four_color.allocate_color(bording_region_dict, results_dict)
        self.assertNotEqual(results_dict['Region_0'], results_dict['Region_1'], "Region_0 cannot have the same color as Region_1" )
        self.assertNotEqual(results_dict['Region_0'], results_dict['Region_2'], "Region_0 cannot have the same color as Region_2" )
        self.assertNotEqual(results_dict['Region_0'], results_dict['Region_3'], "Region_0 cannot have the same color as Region_3" )
        self.assertNotEqual(results_dict['Region_1'], results_dict['Region_2'], "Region_1 cannot have the same color as Region_2" )
        self.assertNotEqual(results_dict['Region_2'], results_dict['Region_3'], "Region_2 cannot have the same color as Region_3" )
        self.assertNotEqual(results_dict['Region_3'], results_dict['Region_4'], "Region_3 cannot have the same color as Region_4" )

if __name__ == '__main__':
    unittest.main()
