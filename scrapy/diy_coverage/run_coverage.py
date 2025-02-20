import unittest
from scrapy.diy_coverage.diycoverage import (
    initialize_coverage,
    report_coverage,
)

if __name__ == "__main__":
    initialize_coverage()

    # Discover and run all tests in /tests directory
    ### --- Some test will throw ERROR due to missing dependencies since
    ### we are omitting the tox enviroment ---
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # Report coverage
    report_coverage()
