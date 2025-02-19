import unittest
from scrapy.diy_coverage.diycoverage import (
    initialize_coverage,
    report_coverage,
)

if __name__ == "__main__":
    initialize_coverage()

    module_paths = [
        "tests.test_exporters",
        "tests.test_spidermiddleware_depth",
        "tests.test_middleware",
        "tests.test_http_request",
        "tests.test_http_cookies",
        "tests.test_http_headers",
        "tests.test_http_response",
    ]

    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all tests from specified test modules
    for module_path in module_paths:
        try:
            tests = loader.loadTestsFromName(module_path)
            suite.addTests(tests)
        except Exception as e:
            print(f"Error loading tests from {module_path}: {e}")

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

    # Report coverage
    report_coverage()
