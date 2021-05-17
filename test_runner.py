import unittest

import os
from html_test_runner import HTMLTestRunner

if __name__=='__main__':
    # get the directory path to output report file
    dir = os.getcwd()

    TestsMain = unittest.TestLoader().loadTestsFromTestCase(TestsMain)

    smoke_tests = unittest.TestSuite([TestsMain])

    outfile = open('C:\\Users\\afinapd\PycharmProjects\\SunterraCX\\Reports' + '\Report_15-02-2021.html', 'wb')

    # configure HTMLTestRunner options
    runnerHTML = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                           title='Test Report',
                                           description='Smoke Tests')

    # run the suite using HTMLTestRunner
    runnerHTML.run(smoke_tests)