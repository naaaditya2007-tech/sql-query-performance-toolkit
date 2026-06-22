import unittest
from query_planner import estimate_query_plan

class TestSQL(unittest.TestCase):
    def test_plan(self):
        self.assertLess(estimate_query_plan(1000, True)["io_cost"], estimate_query_plan(1000, False)["io_cost"])

if __name__ == "__main__":
    unittest.main()
